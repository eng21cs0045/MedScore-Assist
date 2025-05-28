import streamlit as st

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

st.title("📍 Bangalore Location")
st.markdown("""
We are actively serving in **Bangalore** with multiple partnerships and client networks.
- [View on Google Maps](https://www.google.com/maps/place/Bangalore)
""")
