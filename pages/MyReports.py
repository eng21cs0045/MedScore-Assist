import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page

st.markdown(
    """
    <style>
    /* Hide the sidebar completely */
            .css-1d391kg {
                display: none;
            }
            
            .css-1aumxhk {
                display: none;
            }
            
            /* Hide sidebar in newer Streamlit versions */
            section[data-testid="stSidebar"] {
                display: none !important;
            }
            
            /* Hide the sidebar toggle button */
            button[kind="header"] {
                display: none;
            }
            
            /* Adjust main content to take full width when sidebar is hidden */
            .main .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
                max-width: 100%;
            }
    </style>
    """,
    unsafe_allow_html=True)

# ─── Configuration ─────────────────────────────────────────────────────────────
REPORTS_FOLDER = r"reports"
os.makedirs(REPORTS_FOLDER, exist_ok=True)

# ─── Helper ────────────────────────────────────────────────────────────────────
def get_report_files():
    """Retrieve all stored PDF report files."""
    return [f for f in os.listdir(REPORTS_FOLDER) if f.endswith(".pdf")]

# ─── Page ──────────────────────────────────────────────────────────────────────
def my_reports_page():
    st.title("📑 My Reports")
    reports = get_report_files()

    if not reports:
        st.info("No reports available. Run a model to generate a report.")
        return

    st.write("### Your Generated Reports:")
    for report in reports:
        report_path = os.path.join(REPORTS_FOLDER, report)
        report_name = report.replace("_", " ").replace(".pdf", "")

        c1, c2, c3 = st.columns([3, 1, 1])
        with c1:
            st.write(f"📄 **{report_name}**")
        with c2:
            with open(report_path, "rb") as f:
                st.download_button(
                    label="📥 Download",
                    data=f.read(),
                    file_name=report,
                    mime="application/pdf",
                    key=f"dl_{report}"
                )
        with c3:
            if st.button("🗑️ Delete", key=f"del_{report}"):
                os.remove(report_path)
                st.success(f"Deleted {report}")
                st.rerun()

# ─── Back Button ────────────────────────────────────────────────────────────────
if st.button("⬅️ Back to Home"):
    st.switch_page(r"pages/02LandingPage.py")

# ─── Run ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    my_reports_page()
