# AI_USAGE.md

## AI Tools Used

* ChatGPT
* GitHub Copilot

## Example Prompts

1. Generate FastAPI CSV import endpoint
2. Design anomaly detection engine
3. Create Streamlit dashboard

## AI Mistakes Found

### Case 1

Issue:
Amount column imported as string.

Impact:
TypeError during anomaly detection.

Fix:
Added numeric conversion using pandas.

---

### Case 2

Issue:
Incorrect import path.

Impact:
ModuleNotFoundError.

Fix:
Adjusted FastAPI project structure.

---

### Case 3

Issue:
Negative values treated as invalid.

Impact:
Refunds were ignored.

Fix:
Implemented refund handling policy.

## Verification Process

Every generated code block was:

* Reviewed manually
* Tested locally
* Debugged before deployment
