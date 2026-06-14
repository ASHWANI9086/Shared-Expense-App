import pandas as pd
from app.core.db import DB
from app.policies.anomaly_policy import POLICY
from app.services.anomaly_service import detect_anomalies
from app.core.config import USD_TO_INR

class ImportService:

    def process(self, df: pd.DataFrame):

        conn = DB.get_conn()
        cur = conn.cursor()

        cleaned = 0
        anomalies_report = []

        for _, row in df.iterrows():
            row = row.to_dict()

            # Normalize missing values so the response is JSON-safe
            for key, value in row.items():
                if pd.isna(value):
                    row[key] = None

            # SAFE AMOUNT PARSE
            amount_value = row.get("amount", 0)
            try:
                amount = float(str(amount_value).replace(",", ""))
            except (TypeError, ValueError):
                amount = 0.0
            row["amount"] = amount

            anomalies = detect_anomalies(row)

            action_taken = []

            # USD conversion
            if "USD_CURRENCY" in anomalies:
                row["amount"] = amount * USD_TO_INR
                row["currency"] = "INR"
                action_taken.append("CONVERTED_USD_TO_INR")

            # Negative handling
            if "NEGATIVE_AMOUNT" in anomalies:
                action_taken.append("TREATED_AS_REFUND")

            # Insert into DB
            cur.execute("""
                INSERT INTO expenses (
                    date, description, paid_by, amount,
                    currency, split_type, split_with,
                    split_details, notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row.get("date"),
                row.get("description"),
                row.get("paid_by"),
                row.get("amount"),
                row.get("currency"),
                row.get("split_type"),
                row.get("split_with"),
                row.get("split_details"),
                row.get("notes")
            ))

            cleaned += 1

            if anomalies:
                anomalies_report.append({
                    "row": row,
                    "type": ",".join(anomalies),
                    "action": ",".join(action_taken)
                })

        conn.commit()
        conn.close()

        return {
            "total_cleaned": cleaned,
            "total_anomalies": len(anomalies_report),
            "anomalies": anomalies_report
        }