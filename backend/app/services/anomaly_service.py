def detect_anomalies(row):
    anomalies = []

    if row.get("currency") == "USD":
        anomalies.append("USD_CURRENCY")

    amount = float(row.get("amount", 0))

    if amount < 0:
        anomalies.append("NEGATIVE_AMOUNT")

    if not row.get("split_with"):
        anomalies.append("INVALID_SPLIT")

    if "duplicate" in str(row.get("notes", "")).lower():
        anomalies.append("DUPLICATE_ROW")

    return anomalies