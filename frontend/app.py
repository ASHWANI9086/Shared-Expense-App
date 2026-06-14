import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_URL = "http://127.0.0.1:8001/import/csv"

st.set_page_config(
    page_title="ExpenseOS | SaaS Dashboard",
    layout="wide",
    page_icon="💸"
)

# ---------------- THEME CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0B1220;
}

.block-container {
    padding: 2rem 3rem;
}

h1, h2, h3 {
    color: #E5E7EB;
}

.kpi {
    background: #162238;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #22304a;
}

.kpi-title {
    font-size: 13px;
    color: #94A3B8;
}

.kpi-value {
    font-size: 26px;
    font-weight: 700;
    color: #E5E7EB;
}

.card {
    background: #111A2E;
    padding: 16px;
    border-radius: 14px;
    border: 1px solid #1f2a44;
}

.badge-danger {
    background: #EF4444;
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 12px;
    color: white;
}

.badge-warning {
    background: #F59E0B;
    padding: 4px 8px;
    border-radius: 8px;
    font-size: 12px;
    color: black;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("💸 ExpenseOS")
st.caption("AI-powered Shared Expense Intelligence Platform")

# ---------------- UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Expenses CSV", type=["csv"])

if uploaded_file:

    with st.spinner("Analyzing financial data..."):
        res = requests.post(
            API_URL,
            files={"file": (uploaded_file.name, uploaded_file, "text/csv")}
        )

    if res.status_code == 200:
        data = res.json()

        # ---------------- KPI ROW ----------------
        c1, c2, c3, c4 = st.columns(4)

        c1.markdown(f"""
        <div class="kpi">
            <div class="kpi-title">Total Cleaned</div>
            <div class="kpi-value">{data['total_cleaned']}</div>
        </div>
        """, unsafe_allow_html=True)

        c2.markdown(f"""
        <div class="kpi">
            <div class="kpi-title">Anomalies Detected</div>
            <div class="kpi-value">{data['total_anomalies']}</div>
        </div>
        """, unsafe_allow_html=True)

        c3.markdown(f"""
        <div class="kpi">
            <div class="kpi-title">System Status</div>
            <div class="kpi-value">HEALTHY</div>
        </div>
        """, unsafe_allow_html=True)

        c4.markdown(f"""
        <div class="kpi">
            <div class="kpi-title">Engine</div>
            <div class="kpi-value">v2.0</div>
        </div>
        """, unsafe_allow_html=True)

        # ---------------- CHARTS ----------------
        st.markdown("## 📊 Financial Analytics")

        df = pd.DataFrame([a["row"] for a in data["anomalies"]])

        col1, col2 = st.columns(2)

        if not df.empty:
            fig1 = px.bar(df, x="paid_by", y="amount", color="paid_by")
            col1.plotly_chart(fig1, use_container_width=True)

            fig2 = px.pie(df, names="currency", values="amount")
            col2.plotly_chart(fig2, use_container_width=True)

        # ---------------- ANOMALY INTELLIGENCE ----------------
        st.markdown("## ⚠️ Anomaly Intelligence Engine")

        for a in data["anomalies"]:
            st.markdown(f"""
            <div class="card">
                <b>Description:</b> {a['row'].get('description')} <br>
                <b>Type:</b> <span class="badge-warning">{a['type']}</span> <br>
                <b>Action:</b> <span class="badge-danger">{a['action']}</span>
            </div>
            <br>
            """, unsafe_allow_html=True)

        # ---------------- RAW DEBUG ----------------
        with st.expander("Developer View (Raw JSON)"):
            st.json(data)

    else:
        st.error("Backend connection failed")