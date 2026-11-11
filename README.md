# Richie Garafola — Engineering & Analytics Portfolio

**Data Engineering · Financial Analytics · Business Intelligence · Automation**

A curated portfolio of work in data validation, financial reconciliation, repeatable ETL, business intelligence, and earlier quantitative research.

> I build data systems that make complex information reliable, traceable, and actionable.

**[GitHub profile](https://github.com/RichieGarafola) · [LinkedIn](https://www.linkedin.com/in/richiegarafola)**

## Featured applications

| Project | What it demonstrates | Links |
| --- | --- | --- |
| **DeltaAnalysis** | Bidirectional CSV/Excel comparison, field-level change tracking, duplicate-key diagnostics, audit-ready exports | [Source](https://github.com/RichieGarafola/DeltaAnalysis) · [Live app](https://deltaanalysis.streamlit.app) |
| **ReconcileKit** | Invoice-to-payment reconciliation in integer cents, exceptions, append-only reviewer audit trail, SQL reporting, Power BI | [Source](https://github.com/RichieGarafola/ReconcileKit) |
| **ETL Pipeline Builder** | Ordered transformations and auditable execution | [Source](https://github.com/RichieGarafola/etl-pipeline-builder) |
| **Budget Variance Analyzer** | Budget-versus-actual analysis and projections | [Source](https://github.com/RichieGarafola/budget-variance-analyzer) |
| **Financial KPI Dashboard** | Financial performance metrics | [Source](https://github.com/RichieGarafola/financial-kpi-dashboard) |
| **docutil** | Repeatable document conversion and batch processing | [Source](https://github.com/RichieGarafola/docutil) |

## Earlier work

The Streamlit site includes a separate **Earlier Work** section for exploratory and educational projects, including forex correlation, Fama–French factors, GARCH, hidden Markov models, banking dashboards, and forecasting. These are historical learning artifacts, not claims of production-grade or predictive performance.

## Run locally

The application entry point is `site.py`.

```bash
python -m venv .venv
# Activate .venv using your shell's activation command.
python -m pip install -r requirements.txt
python -m streamlit run site.py
```

The site uses Streamlit and Python standard-library utilities only. Remote project links and images may need internet access; the app does not require API keys.

## Deployment

If deploying on Streamlit Community Cloud, configure **`site.py`** as the main file. The older hosted URL in the original README has not been independently verified; do not treat it as a confirmed active deployment.

## Design and data notes

- The modernized app keeps featured engineering projects separate from older educational research.
- Project descriptions link directly to their source repositories for verification.
- Demo datasets are synthetic or fixed-seed generated where documented by the underlying projects.
- No employer/client data should be added to this public site.
- The original Streamlit implementation remains accessible in Git history.

## Next improvements

- Verify deployment and public links after merging.
- Add screenshots of the actual DeltaAnalysis UI when a stable image is available.
- Add lightweight application smoke tests and CI.
- Review and modernize selected earlier repositories independently, keeping their history intact.
