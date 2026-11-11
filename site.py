"""A screenshot-first, source-linked data engineering portfolio.

Intentionally dependency-light: uses Streamlit and the standard library only.
Remote screenshots come from the associated public GitHub repositories.
"""

import html

import streamlit as st


st.set_page_config(
    page_title="Richie Garafola | Data Engineering & Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

GITHUB = "https://github.com/RichieGarafola"
LINKEDIN = "https://www.linkedin.com/in/richiegarafola"
RAW = "https://raw.githubusercontent.com/RichieGarafola"

PROJECTS = [
    {
        "name": "DeltaAnalysis",
        "category": "Data engineering & quality",
        "eyebrow": "FLAGSHIP · DATA RECONCILIATION",
        "summary": (
            "Trace additions, removals, duplicates, and field-level changes across "
            "CSV and Excel snapshots. Create an audit-ready comparison workbook."
        ),
        "outcome": "From two source files to a defensible change report.",
        "stack": "Python  ·  pandas  ·  Streamlit  ·  Excel",
        "image": f"{RAW}/DeltaAnalysis/main/docs/screenshots/03_results_dashboard.png",
        "caption": "Actual application results dashboard",
        "repo": f"{GITHUB}/DeltaAnalysis",
        "demo": "https://deltaanalysis.streamlit.app/",
        "demo_label": "Open live demo",
    },
    {
        "name": "ReconcileKit",
        "category": "Financial controls",
        "eyebrow": "FLAGSHIP · FINANCIAL RECONCILIATION",
        "summary": (
            "Reconcile invoices and payments with integer-cent accuracy, "
            "data-quality exceptions, auditable reviewer actions, and BI views."
        ),
        "outcome": "Built for traceable financial exception workflows.",
        "stack": "Python  ·  DuckDB  ·  Parquet  ·  Power BI",
        "image": f"{RAW}/ReconcileKit/main/powerbi/screenshots/1-reconciliation-overview.png",
        "caption": "Actual Power BI report screenshot",
        "repo": f"{GITHUB}/ReconcileKit",
        "demo": None,
    },
    {
        "name": "ForexCorrelationMatrix",
        "category": "Quantitative analytics",
        "eyebrow": "FINANCIAL RESEARCH · FX",
        "summary": (
            "Analyze currency-pair co-movement using aligned percentage returns "
            "with sample-size diagnostics, CSV uploads, and an offline demo."
        ),
        "outcome": "Market research with explicit assumptions and limitations.",
        "stack": "Python  ·  pandas  ·  matplotlib  ·  Streamlit",
        "image": f"{RAW}/ForexCorrelationMatrix/main/Images/CorrelationMatrix.png",
        "caption": "Historical screenshot; interface has since been modernized",
        "repo": f"{GITHUB}/ForexCorrelationMatrix",
        "demo": "https://forexcorrelationmatrix.streamlit.app/",
        "demo_label": "Open live demo",
    },
    {
        "name": "BankingCustomerInsights",
        "category": "Business intelligence",
        "eyebrow": "SAMPLE DATA · CUSTOMER ANALYTICS",
        "summary": (
            "Explore customer demographics, account balances, and deposit "
            "subscription outcomes using source-grounded, filterable KPIs."
        ),
        "outcome": "Descriptive analytics without fabricated live-data claims.",
        "stack": "Python  ·  pandas  ·  Plotly  ·  Streamlit",
        "image": f"{RAW}/BankingCustomerInsights/main/Images/app.png",
        "caption": "Historical screenshot; interface has since been modernized",
        "repo": f"{GITHUB}/BankingCustomerInsights",
        "demo": "https://bankingcustomers.streamlit.app/",
        "demo_label": "Published app URL",
    },
    {
        "name": "ETL Pipeline Builder",
        "category": "Data engineering & quality",
        "eyebrow": "DATA PIPELINES · AUTOMATION",
        "summary": (
            "Build and run repeatable CSV transformations with ordered steps, "
            "row-count reporting, and execution-time audit details."
        ),
        "outcome": "Transparent data preparation, not a black-box script.",
        "stack": "Python  ·  ETL  ·  validation",
        "image": f"{RAW}/etl-pipeline-builder/main/screenshots/01_overview.png",
        "caption": "Repository application screenshot",
        "repo": f"{GITHUB}/etl-pipeline-builder",
        "demo": None,
    },
    {
        "name": "Financial KPI Dashboard",
        "category": "Business intelligence",
        "eyebrow": "PERFORMANCE REPORTING · KPI",
        "summary": (
            "Turn financial statement periods into consistent KPIs and "
            "period-over-period views for faster performance review."
        ),
        "outcome": "Decision-ready financial performance reporting.",
        "stack": "Python  ·  financial analytics  ·  reporting",
        "image": f"{RAW}/financial-kpi-dashboard/main/screenshots/01_overview.png",
        "caption": "Repository application screenshot",
        "repo": f"{GITHUB}/financial-kpi-dashboard",
        "demo": None,
    },
]

ADDITIONAL_PROJECTS = [
    ("Budget Variance Analyzer", "Budget-versus-actual review and projections", f"{GITHUB}/budget-variance-analyzer"),
    ("docutil", "DOCX and Markdown conversion automation", f"{GITHUB}/docutil"),
]

EARLIER_WORK = [
    ("Fama–French Risk Model", "Exploring equity factor exposures", "FamaFrenchRiskModel"),
    ("GARCH Volatility", "Exploring volatility modeling assumptions", "GARCH"),
    ("Hidden Markov Model", "Educational financial-market regime modeling", "HiddenMarkovModel"),
    ("Asset Price Prediction", "Historical time-series forecasting experiment", "AssetPricePrediction"),
    ("Basic Stock Analysis", "Foundational financial data analysis", "BasicStockAnalysis"),
]

CSS = """
<style>
:root { --accent: #087f8c; --muted: #64748b; }
.block-container { max-width: 1240px; padding-top: 2.2rem; padding-bottom: 4rem; }
.hero-kicker { font-size: .77rem; font-weight: 750; letter-spacing: .16em;
  text-transform: uppercase; color: var(--accent); margin-bottom: .75rem; }
.hero-title { font-size: clamp(2.5rem, 5vw, 4.2rem); font-weight: 800;
  letter-spacing: -.045em; line-height: 1.08; margin: 0 0 1rem; }
.hero-copy { font-size: clamp(1.05rem, 2vw, 1.25rem); line-height: 1.7;
  max-width: 760px; opacity: .82; margin-bottom: 1.2rem; }
.section-kicker { color: var(--accent); text-transform: uppercase;
  letter-spacing: .14em; font-size: .74rem; font-weight: 800; margin-bottom: .25rem; }
.project-kicker { text-transform: uppercase; font-size: .72rem;
  letter-spacing: .13em; color: var(--accent); font-weight: 750; }
.project-outcome { border-left: 3px solid var(--accent); padding-left: .85rem;
  margin: .8rem 0; font-size: .94rem; opacity: .86; }
.project-stack { font-size: .80rem; color: var(--muted); line-height: 1.6;
  margin-top: .3rem; margin-bottom: 1rem; }
.mini-note { font-size: .82rem; color: var(--muted); }
[data-testid="stVerticalBlockBorderWrapper"] { border-radius: 14px; }
[data-testid="stImage"] img { border-radius: 10px; }
[data-testid="stSidebar"] { border-right: 1px solid rgba(128,128,128,.12); }
@media (max-width: 700px) {
  .block-container { padding-top: 1.1rem; }
  .hero-title { font-size: 2.55rem; }
}
</style>
"""


def plain(text: str) -> str:
    """Encode dynamic text before rendering it in minimal decorative HTML."""
    return html.escape(text, quote=True)


def project_card(project: dict) -> None:
    """Show authentic repository imagery alongside source-linked project context."""
    with st.container(border=True):
        image_col, details_col = st.columns([1.08, 1], gap="large")
        with image_col:
            st.image(
                project["image"],
                caption=project["caption"],
                use_container_width=True,
            )
        with details_col:
            st.markdown(
                f'<p class="project-kicker">{plain(project["eyebrow"])}</p>',
                unsafe_allow_html=True,
            )
            st.subheader(project["name"])
            st.write(project["summary"])
            st.markdown(
                f'<p class="project-outcome">{plain(project["outcome"])}</p>',
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<div class="project-stack">{plain(project["stack"])}</div>',
                unsafe_allow_html=True,
            )
            source, live = st.columns(2)
            with source:
                st.link_button("View source", project["repo"], use_container_width=True)
            with live:
                if project.get("demo"):
                    st.link_button(
                        project.get("demo_label", "View app"),
                        project["demo"],
                        use_container_width=True,
                    )


st.markdown(CSS, unsafe_allow_html=True)
st.markdown('<p class="hero-kicker">Engineering portfolio / Richie Garafola</p>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Turning complex data into<br>clear decisions.</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-copy">I build reliable, traceable data workflows—from '
    'reconciliation and data quality to financial reporting, business intelligence, '
    'and pragmatic automation.</p>',
    unsafe_allow_html=True,
)
st.caption("New York · Open to fully remote data, reporting, and automation opportunities")

primary, secondary, tertiary = st.columns([1, 1, 1], gap="small")
with primary:
    st.link_button("Explore GitHub", GITHUB, use_container_width=True)
with secondary:
    st.link_button("Connect on LinkedIn", LINKEDIN, use_container_width=True)
with tertiary:
    st.link_button(
        "Try DeltaAnalysis", "https://deltaanalysis.streamlit.app/", use_container_width=True
    )

st.divider()
view = st.sidebar.radio(
    "Explore",
    ["Featured Projects", "Earlier Work", "About & Contact"],
    index=0,
)
st.sidebar.caption("Engineering · Analytics · Financial reporting")
st.sidebar.markdown(f"[GitHub profile]({GITHUB})")
st.sidebar.markdown(f"[LinkedIn]({LINKEDIN})")

if view == "Featured Projects":
    st.markdown('<p class="section-kicker">Selected engineering work</p>', unsafe_allow_html=True)
    st.header("Featured projects")
    st.write(
        "Source-linked projects with real application and reporting screenshots. "
        "Select a focus area or explore the full collection."
    )
    categories = ["All categories"] + sorted({p["category"] for p in PROJECTS})
    selected = st.selectbox("Filter by focus area", categories)
    visible = [
        p for p in PROJECTS
        if selected == "All categories" or selected == p["category"]
    ]
    st.caption(f"Showing {len(visible)} of {len(PROJECTS)} featured projects")

    for project in visible:
        project_card(project)

    st.subheader("More tools & automation")
    for name, summary, url in ADDITIONAL_PROJECTS:
        st.markdown(f"**[{name}]({url})** — {summary}")

    st.caption(
        "Screenshot captions distinguish current views from historical interfaces. "
        "Sample and synthetic datasets are described in their respective repositories. "
        "No protected client or employer data is presented here."
    )

elif view == "Earlier Work":
    st.markdown('<p class="section-kicker">Quantitative foundations</p>', unsafe_allow_html=True)
    st.header("Earlier quantitative research & learning projects")
    st.write(
        "These educational repositories record my progression through financial-market "
        "research and Python. They are not advertised as validated trading systems."
    )
    for title, description, slug in EARLIER_WORK:
        with st.expander(title):
            st.write(description)
            st.markdown(f"[View repository]({GITHUB}/{slug})")

else:
    st.markdown('<p class="section-kicker">Background & connection</p>', unsafe_allow_html=True)
    st.header("About")
    st.write(
        "My background combines federal financial and operational reporting with "
        "Python, data engineering, and business intelligence. I focus on trustworthy "
        "inputs, reproducible calculations, and outputs that stand up to review."
    )
    left, right = st.columns([1.2, 1], gap="large")
    with left:
        st.subheader("Technical toolkit")
        st.markdown(
            "**Engineering:** Python · pandas · SQL · PostgreSQL · DuckDB · ETL  \n"
            "**Analytics & BI:** Power BI · DAX · Power Query · Excel  \n"
            "**Delivery:** Streamlit · REST APIs · pytest · GitHub Actions"
        )
        st.subheader("Working principles")
        st.write(
            "Document assumptions. Validate inputs. Surface exceptions. "
            "Make calculations reproducible. Present findings clearly."
        )
    with right:
        with st.container(border=True):
            st.subheader("Background")
            st.write("B.S. Computer Science — Capella University (2026)")
            st.write("Arizona State University FinTech Bootcamp")
            st.write("CompTIA Project+")
        with st.container(border=True):
            st.subheader("Get in touch")
            st.write("Interested in fully remote data engineering, reporting, and automation work.")
            st.link_button("Connect on LinkedIn", LINKEDIN, use_container_width=True)
            st.link_button("Browse repositories", GITHUB, use_container_width=True)
