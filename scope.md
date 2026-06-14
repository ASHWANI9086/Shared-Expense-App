# SCOPE.md

## Database Schema

Users

* id
* name
* email

Groups

* id
* group_name

Memberships

* id
* user_id
* group_id
* joined_at
* left_at

Expenses

* id
* date
* description
* paid_by
* amount
* currency
* split_type

Settlements

* id
* payer
* receiver
* amount

---

## Anomalies Detected

### 1. USD Currency Entries

Problem:
Expense recorded in USD but treated as INR.

Action:
Converted USD → INR using configured exchange rate.

### 2. Negative Amounts

Problem:
Negative expense values.

Action:
Treated as refunds instead of expenses.

### 3. Duplicate Expenses

Problem:
Same expense recorded multiple times.

Action:
Flagged for manual review.

### 4. Member Not Active

Problem:
Expense assigned to inactive member.

Action:
Flagged and excluded from balance calculations.

### 5. Missing Split Details

Problem:
Split participants missing.

Action:
Marked anomaly and requested review.

### 6. Invalid Date Format

Problem:
Inconsistent date formatting.

Action:
Normalized during import.

### 7. Settlement Logged as Expense

Problem:
Repayment recorded as expense.

Action:
Converted to settlement transaction.

### 8. Unknown Member

Problem:
Expense references non-existing member.

Action:
Flagged for review.

### 9. Blank Description

Problem:
Missing expense description.

Action:
Imported with warning.

### 10. Unsupported Currency

Problem:
Currency not recognized.

Action:
Flagged anomaly.

### 11. Future Date

Problem:
Expense date after current date.

Action:
Flagged anomaly.

### 12. Inconsistent Split Values

Problem:
Split percentages not totaling 100%.

Action:
Flagged and blocked auto-processing.
