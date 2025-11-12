from flask import Flask, render_template, request, abort
from report.report import get_common_stats, get_drivers, get_driver_info
from datetime import datetime

app = Flask(__name__)


@app.context_processor
def inject_now():
    return {'current_year': datetime.now().year}

@app.route('/')
def home_page():
    """Home page - entry point."""
    return render_template("home.html", title="Monaco 2018 Racing Report")

@app.route("/report")
def report_page():
    """Main report page - shows common race statistics"""
    order = request.args.get("order", "asc")
    good, bad = get_common_stats(order)
    return render_template("report.html", good=good, bad=bad, order=order)


@app.route("/report/drivers/")
def drivers_page():
    """Show list of drivers with links to their profiles."""
    order = request.args.get("order", "asc")
    drivers = get_drivers(order)
    return render_template("drivers.html", drivers=drivers, order=order)


@app.route("/report/drivers/<driver_id>")
def driver_page(driver_id):
    """Show details about a specific driver."""
    info = get_driver_info(driver_id)
    if not info:
        abort(404, f"Driver with id '{driver_id}' not found.")
    return render_template("driver.html", driver=info)


if __name__ == "__main__":
    app.run(debug=True)