# DECISIONS.md

## Decision 1

Problem:
How to handle negative amounts?

Options:

1. Reject import
2. Treat as refund

Chosen:
Treat as refund

Reason:
Preserves transaction history.

---

## Decision 2

Problem:
How to handle USD expenses?

Options:

1. Ignore currency
2. Convert currency

Chosen:
Convert USD to INR

Reason:
Required by business rules.

---

## Decision 3

Problem:
How to handle duplicates?

Options:

1. Delete automatically
2. Flag for review

Chosen:
Flag for review

Reason:
User approval required.

---

## Decision 4

Problem:
How to manage member joins/leaves?

Chosen:
Store membership dates.

Reason:
Ensures historical accuracy.

---

## Decision 5

Problem:
Database selection

Chosen:
SQLite

Reason:
Simple relational database satisfying assignment requirements.
