"""Headless checks for the screenshot-first portfolio and navigation."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


ENTRY = str(Path(__file__).resolve().parents[1] / "site.py")


def test_featured_page_renders_source_linked_projects():
    app = AppTest.from_file(ENTRY, default_timeout=45).run()
    assert not app.exception
    assert any("Turning complex data into" in item.value for item in app.markdown)
    subheadings = [item.value for item in app.subheader]
    assert "DeltaAnalysis" in subheadings
    assert "ReconcileKit" in subheadings
    assert "ForexCorrelationMatrix" in subheadings
    assert len(app.selectbox) == 1
    assert app.selectbox[0].value == "All categories"


def test_featured_filter_keeps_appropriate_project():
    app = AppTest.from_file(ENTRY, default_timeout=45).run()
    app.selectbox[0].set_value("Financial controls").run()
    assert not app.exception
    titles = [item.value for item in app.subheader]
    assert "ReconcileKit" in titles
    assert "DeltaAnalysis" not in titles


def test_earlier_work_and_about_navigation():
    app = AppTest.from_file(ENTRY, default_timeout=45).run()
    app.sidebar.radio[0].set_value("Earlier Work").run()
    assert not app.exception
    assert any("Earlier quantitative research" in item.value for item in app.header)
    app.sidebar.radio[0].set_value("About & Contact").run()
    assert not app.exception
    assert any(item.value == "About" for item in app.header)
    assert any(item.value == "Technical toolkit" for item in app.subheader)
