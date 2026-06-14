# Shared Expense App

A production-ready Shared Expense Management application inspired by Splitwise, built to solve real-world expense tracking problems involving changing group memberships, multiple currencies, inconsistent spreadsheet data, and transparent balance calculations.

## Live Demo

Frontend:
https://shared-expense-app-bmrsk2xpqdauyctul4uie7.streamlit.app/

Backend API:
https://shared-expense-app-ttsf.onrender.com

## GitHub Repository

https://github.com/ASHWANI9086/Shared-Expense-App

---

## Problem Statement

A group of flatmates tracked shared expenses using spreadsheets. Over time the spreadsheet became difficult to manage because of:

* Duplicate entries
* Inconsistent data formats
* Currency mismatches (USD and INR)
* Refunds recorded as expenses
* Membership changes over time
* Lack of transparency in balance calculations

The objective was to build an application that can import raw expense data, detect anomalies, generate import reports, and provide clear expense summaries.

---

## Features

### CSV Import Engine

* Upload expense CSV directly
* No manual CSV editing required
* Automatic parsing and validation
* Import summary generation

### Anomaly Detection

The system detects and reports:

* USD currency entries
* Negative amount transactions (refunds)
* Invalid values
* Missing fields
* Data inconsistencies

Each anomaly is surfaced to the user along with the action taken.

### Balance Calculation

* Equal expense splitting
* Per-user share computation
* Net balance calculation
* Expense traceability

### Transparent Reporting

* Total imported records
* Total anomalies detected
* Detailed anomaly log
* Action taken for every anomaly

### Dashboard

* Modern Streamlit interface
* Upload workflow
* Import reports
* Summary cards
* Interactive tables

---

## Tech Stack

### Frontend

* Streamlit
* Plotly
* Pandas

### Backend

* FastAPI
* Python
* Uvicorn

### Database

* SQLite

### Deployment

* Render (Backend)
* Streamlit Cloud (Frontend)

---

## Project Structure

```text
Shared-Expense-App/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── policies/
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── frontend/
│   └── app.py
│
├── README.md
├── SCOPE.md
├── DECISIONS.md
├── AI_USAGE.md
└── requirements.txt
```

## Import Workflow

1. User uploads CSV file.
2. Backend parses all rows.
3. Validation engine checks anomalies.
4. Policy engine decides handling strategy.
5. Import report is generated.
6. Dashboard displays results.

---

## Example

### Input

```text
Date: 12-03-2026
Description: Parasailing Refund
Amount: -2490
Currency: USD
```

### Detected Issues

```text
NEGATIVE_AMOUNT
USD_CURRENCY
```

### Action Taken

```text
TREATED_AS_REFUND
CONVERTED_USD_TO_INR
```

---

## API Endpoints

### Import CSV

POST

```text
/import/csv
```

Accepts:

```text
multipart/form-data
```

Response:

```json
{
  "total_cleaned": 42,
  "total_anomalies": 4,
  "anomalies": []
}
```

---

## Setup Instructions

### Clone Repository

```bash
git clone https://github.com/ASHWANI9086/Shared-Expense-App.git
cd Shared-Expense-App
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
cd backend
python -m uvicorn app.main:app --reload --port 8001
```

Swagger:

```text
http://localhost:8001/docs
```

---

## Run Frontend

```bash
streamlit run frontend/app.py
```

---

## Design Principles

* No silent data modification
* Every anomaly must be visible
* User should understand every calculation
* Policy-driven data cleaning
* Reproducible imports

---

## Documentation

### SCOPE.md

Contains:

* Anomaly catalog
* Data cleaning policies
* Database schema

### DECISIONS.md

Contains:

* Engineering decisions
* Trade-off analysis
* Alternative approaches considered

### AI_USAGE.md

Contains:

* AI tools used
* Prompts used
* AI mistakes discovered
* Corrections made

---

## Future Improvements

* Authentication system
* Group management
* Dynamic member join/leave history
* Settlement tracking
* Audit trail
* Approval workflow for anomaly resolution
* Multi-currency exchange rate service
* Advanced balance explanations

---

## AI Usage

This project was developed using AI-assisted development. All generated code was reviewed, tested, modified, and validated before inclusion in the final solution. The developer remains responsible for all implementation decisions and submitted code.

---

## Author

Ashwani Kumar

Registration Number: 12319687

B.Tech CSE (AI & ML)

Lovely Professional University
