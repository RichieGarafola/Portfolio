# Richie Garafola | Data Engineering & Analytics

A curated, screenshot-first portfolio of practical work in **data engineering, financial reconciliation, business intelligence, and automation**.

> Reliable inputs. Traceable calculations. Decision-ready outputs.

[GitHub profile](https://github.com/RichieGarafola) · [LinkedIn](https://www.linkedin.com/in/richiegarafola) · [DeltaAnalysis demo](https://deltaanalysis.streamlit.app/)

## Portfolio highlights

The Streamlit landing page opens with a concise professional introduction and direct links to featured work. Project cards include genuine screenshots sourced from the corresponding public repositories, an outcome statement, technical stack, and repository links.

| Featured project | Primary focus | Screenshot source |
| --- | --- | --- |
| [DeltaAnalysis](https://github.com/RichieGarafola/DeltaAnalysis) | Audit-ready file comparison and reconciliation | [Application results](https://github.com/RichieGarafola/DeltaAnalysis/blob/main/docs/screenshots/03_results_dashboard.png) |
| [ReconcileKit](https://github.com/RichieGarafola/ReconcileKit) | Financial exception handling and auditability | [Power BI overview](https://github.com/RichieGarafola/ReconcileKit/blob/main/powerbi/screenshots/1-reconciliation-overview.png) |
| [ForexCorrelationMatrix](https://github.com/RichieGarafola/ForexCorrelationMatrix) | Return-based FX correlation analysis | [Historical screenshot](https://github.com/RichieGarafola/ForexCorrelationMatrix/blob/main/Images/CorrelationMatrix.png) |
| [BankingCustomerInsights](https://github.com/RichieGarafola/BankingCustomerInsights) | Source-grounded customer analytics | [Historical screenshot](https://github.com/RichieGarafola/BankingCustomerInsights/blob/main/Images/app.png) |
| [ETL Pipeline Builder](https://github.com/RichieGarafola/etl-pipeline-builder) | Repeatable transformations and validation | [Application overview](https://github.com/RichieGarafola/etl-pipeline-builder/blob/main/screenshots/01_overview.png) |
| [Financial KPI Dashboard](https://github.com/RichieGarafola/financial-kpi-dashboard) | Financial performance reporting | [Application overview](https://github.com/RichieGarafola/financial-kpi-dashboard/blob/main/screenshots/01_overview.png) |

**Also featured:** [Budget Variance Analyzer](https://github.com/RichieGarafola/budget-variance-analyzer) and [docutil](https://github.com/RichieGarafola/docutil).

**Historical screenshot disclosure:** The Forex and Banking images originate from older versions of their applications. Their cards explicitly identify these screenshots as historical rather than representing the current UI.

## Run locally

Python 3.10 or 3.11:

```bash
python -m venv .venv
# Activate the virtual environment using your operating system's shell.
python -m pip install -r requirements.txt
python -m streamlit run site.py
```

The site needs no API keys, database, or secrets. Screenshots are loaded over HTTPS from GitHub's publicly hosted raw image files, so an internet connection is required to display them. No application data is fetched at startup.

## Automated checks

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

GitHub Actions tests the portfolio on Python 3.10 and 3.11. The smoke tests cover the default featured view, category filtering, and navigation between earlier work and the About page.

## Deploy on Streamlit Community Cloud

Select the **main** branch and **site.py** entry point in `RichieGarafola/Portfolio`.

> Important: the repository retains an older, divergent `master` branch. Deploying `master` will serve the obsolete portfolio with incompatible old dependencies. The modernized app lives on `main`.

`requirements.txt` pins a compatible Streamlit/Altair pair to prevent the previously reported `altair.vegalite.v4` import error on the old deployment.

## Data, claims, and image provenance

- Links point to the original source repositories for independent inspection.
- Real screenshots are not generated mockups; project captions distinguish historical UIs where needed.
- Public examples may use synthetic or sample datasets as described in their individual repositories.
- Do not upload confidential customer, government, or employer data to these public apps.
- Earlier research is intentionally kept in a separate section and not described as production trading systems.

## Design choices

The visual upgrade uses Streamlit built-ins and a small amount of presentation CSS. It avoids extra front-end dependencies and keeps the original navigation and project-history structure for maintainability. The source of truth for project links and card descriptions is the `PROJECTS` collection in `site.py`.
