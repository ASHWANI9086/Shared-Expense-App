# Shared Expense App

A production-ready Shared Expense Management Application inspired by Splitwise.

## Features

* CSV Import Engine
* Anomaly Detection & Resolution
* Multi-member Expense Splitting
* Balance Calculation
* Settlement Tracking
* Audit-Friendly Import Reports
* FastAPI Backend
* Streamlit Dashboard
* SQLite Relational Database

## Tech Stack

Backend:

* FastAPI
* SQLAlchemy
* SQLite

Frontend:

* Streamlit
* Plotly

Deployment:

* Render (Backend)
* Streamlit Cloud (Frontend)

## Setup

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload --port 8001
```

### Frontend

```bash
cd frontend

streamlit run app.py
```

## Import Workflow

1. Upload expenses_export.csv
2. Detect anomalies
3. Generate import report
4. Calculate balances
5. Display settlement summary

## AI Usage

AI was used as a development assistant. All generated code was reviewed, modified, tested, and validated manually before submission.

## Deployment

Backend:
https://shared-expense-app-ttsf.onrender.com

Frontend:
(Add Streamlit URL Here)
