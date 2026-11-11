"""A curated, source-linked portfolio of data and analytical engineering work."""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Richie Garafola | Data Engineering & Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parent
GITHUB = "https://github.com/RichieGarafola"
LINKEDIN = "https://www.linkedin.com/in/richiegarafola"

PROJECTS = [
    {
        "name": "DeltaAnalysis",
        "category": "Data Engineering & Quality",
        "summary": "Compare CSV and Excel snapshots to trace added, removed, and changed records. Handle duplicate and missing keys and export an auditable, multi-sheet workbook.",
        "stack": "Python · pandas · openpyxl · Streamlit",
        "repo": f"{GITHUB}/DeltaAnalysis",
        "demo": "https://deltaanalysis.streamlit.app",
    },
    {
        "name": "ReconcileKit",
        "category": "Financial Reconciliation",
        "summary": "Reconcile invoices to payments using integer-cent arithmetic, quarantined exceptions, append-only reviewer decisions, SQL views, and a Power BI report.",
        "stack": "Python · DuckDB · Parquet · Power BI · Streamlit",
        "repo": f"{GITHUB}/ReconcileKit",
        "image": "https://raw.githubusercontent.com/RichieGarafola/ReconcileKit/main/powerbi/screenshots/1-reconciliation-overview.png",
    },
    {
        "name": "ETL Pipeline Builder",
        "category": "Data Engineering & Quality",
        "summary": "Run repeatable ordered CSV transformations with an audit trail of row counts and execution times.",
        "stack": "Python · ETL · Data Validation",
        "repo": f"{GITHUB}/etl-pipeline-builder",
    },
    {
        "name": "Budget Variance Analyzer",
        "category": "Financial Analytics",
        "summary": "Compare budget to actuals across departments, categories, and months and estimate year-end spending.",
        "stack": "Python · Financial Reporting",
        "repo": f"{GITHUB}/budget-variance-analyzer",
    },
    {
        "name": "Financial KPI Dashboard",
        "category": "Business Intelligence",
        "summary": "Calculate 17 financial KPIs from period financial statements with period-over-period comparisons.",
        "stack": "Python · Financial Analytics",
        "repo": f"{GITHUB}/financial-kpi-dashboard",
    },
    {
        "name": "docutil",
        "category": "Automation",
        "summary": "Automate DOCX and Markdown conversion for repeatable document processing workflows.",
        "stack": "Python · CLI · Automation",
        "repo": f"{GITHUB}/docutil",
    },
]

EARLIER_WORK = [
    ("Forex Correlation Matrix", "Interactive historical currency-pair correlation analysis.", "ForexCorrelationMatrix"),
    ("Banking Customer Insights", "A Streamlit customer-data dashboard with simulated updates.", "BankingCustomerInsights"),
    ("Fama–French Risk Model", "Exploration of factor exposures and portfolio risk contributions.", "FamaFrenchRiskModel"),
    ("GARCH Volatility", "A quantitative research notebook exploring conditional volatility.", "GARCH"),
    ("Hidden Markov Model", "An educational example exploring inferred financial-market regimes.", "HiddenMarkovModel"),
    ("Asset Price Prediction", "A historical time-series forecasting experiment, not a validated trading system.", "AssetPricePrediction"),
    ("Basic Stock Analysis", "An introductory stock-market data analysis tutorial.", "BasicStockAnalysis"),
]


def project_card(project: dict) -> None:
    """Render a project without fetching remote data at app startup."""
    with st.container(border=True):
        st.subheader(project["name"])
        st.caption(project["category"])
        st.write(project["summary"])
        st.caption(project["stack"])
        st.markdown(f"[View repository]({project['repo']})")
        if demo := project.get("demo"):
            st.markdown(f"[Open live demo]({demo})")
        if image := project.get("image"):
            st.image(image, caption="Project screenshot — synthetic demonstration data", use_container_width=True)


st.title("Richie Garafola")
st.markdown("**Data Engineering · Financial Analytics · Business Intelligence · Automation**")
st.write(
    "I build reliable, traceable data systems—from source validation and reconciliation "
    "to automated reporting and decision-ready analytics."
)
st.caption("New York · Open to fully remote opportunities")
st.markdown(f"[GitHub]({GITHUB}) · [LinkedIn]({LINKEDIN})")
st.divider()

view = st.sidebar.radio(
    "Explore",
    ["Featured Projects", "Earlier Work", "About & Contact"],
    index=0,
)
st.sidebar.caption("A curated portfolio of current engineering and earlier research.")

if view == "Featured Projects":
    st.header("Featured projects")
    st.write(
        "Selected projects emphasize practical data quality, reproducible workflows, "
        "financial controls, and useful reporting."
    )
    categories = ["All categories"] + sorted({p["category"] for p in PROJECTS})
    selected = st.selectbox("Filter by focus area", categories)
    visible = [p for p in PROJECTS if selected == "All categories" or p["category"] == selected]
    for start in range(0, len(visible), 2):
        left, right = st.columns(2, gap="medium")
        with left:
            project_card(visible[start])
        if start + 1 < len(visible):
            with right:
                project_card(visible[start + 1])
    st.info(
        "Public sample datasets are synthetic or generated from fixed seeds where documented "
        "in their repositories. These examples do not include employer or client records."
    )

elif view == "Earlier Work":
    st.header("Earlier quantitative research & learning projects")
    st.write(
        "These repositories document my progression through financial markets, statistical "
        "modeling, and applied Python. They are historical or educational examples, not "
        "claims of production readiness or live predictive performance."
    )
    for title, description, slug in EARLIER_WORK:
        with st.expander(title):
            st.write(description)
            st.markdown(f"[View original repository]({GITHUB}/{slug})")
    st.caption("Historical projects are preserved as-is unless separately modernized and tested.")

else:
    st.header("About")
    st.write(
        "My work combines federal financial and operational reporting experience with "
        "hands-on Python development, analytics, automation, and data-engineering practices. "
        "I focus on systems that make their calculations and underlying records explainable."
    )
    st.subheader("Technical toolkit")
    st.markdown("**Data:** Python, pandas, SQL, PostgreSQL, DuckDB, Parquet, ETL and validation")
    st.markdown("**BI:** Power BI, DAX, Power Query, Excel, financial and operational reporting")
    st.markdown("**Engineering:** pytest, GitHub Actions, Git, Docker, Streamlit, REST APIs")
    st.subheader("Education & certification")
    st.write("B.S. Computer Science — Capella University (2026)")
    st.write("Arizona State University FinTech Bootcamp · CompTIA Project+")
    st.subheader("Connect")
    st.write("Interested in fully remote data engineering, analytics engineering, BI, or automation work.")
    st.markdown(f"[Connect on LinkedIn]({LINKEDIN}) · [Explore GitHub]({GITHUB})")
