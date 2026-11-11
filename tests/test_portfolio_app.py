"""Headless Streamlit smoke tests for all portfolio navigation views."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


ENTRY = Path(__file__).resolve().parents[1] / "site.py"


def test_featured_projects_page_renders():
    app = AppTest.from_file(str(ENTRY), default_timeout=30).run()
    assert not app.exception
    assert app.title[0].value == "Richie Garafola"
    subheadings = [entry.value for entry in app.subheader]
    assert "DeltaAnalysis" in subheadings
    assert "ReconcileKit" in subheadings


def test_earlier_work_and_about_navigation():
    app = AppTest.from_file(str(ENTRY), default_timeout=30).run()
    app.sidebar.radio[0].set_value("Earlier Work").run()
    assert not app.exception
    assert any("Earlier quantitative research" in item.value for item in app.header)
    app.sidebar.radio[0].set_value("About & Contact").run()
    assert not app.exception
    assert any(item.value == "About" for item in app.header)
