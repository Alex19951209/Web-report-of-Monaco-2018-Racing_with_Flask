# 🏎️ Monaco 2018 Racing Web Report

A Flask-based web application that generates a **Formula 1 Monaco Grand Prix 2018 report**  
from raw racing log files — featuring driver statistics, timing data, and sortable tables.

---

## 🚀 Project Overview

This project demonstrates:
- Building a modular web app using **Flask**
- Rendering HTML via **Jinja2** templates
- Separating business logic (`report/`) from presentation (`templates/`)
- Writing unit tests with **pytest** and **BeautifulSoup**

---

## 🌐 Available Routes

| URL | Description |
|-----|--------------|
| `/` | Home page with project overview and navigation |
| `/report` | Common race statistics (drivers, teams, lap times) |
| `/report?order=desc` | Same report, sorted in descending order |
| `/report/drivers/` | List of all drivers with names, codes, and teams |
| `/report/drivers/<driver_id>` | Detailed information about a specific driver |


---

## ⚙️ Setup and Run

### 1️⃣Create a virtual environment:
python -m venv venv

2️⃣Create a virtual environment:
python -m venv venv

3️⃣Activate it:
venv\Scripts\activate

3️⃣Install dependencies:
pip install -r requirements.txt

4️⃣Run the Flask app:
python app.py

Then open your browser at:
👉 http://127.0.0.1:5000/

Run all tests:
pytest -q
