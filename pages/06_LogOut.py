import streamlit as st
import time
def handle_logout():
    # Clear all session state variables
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    
    # Optional: Add a small delay to ensure clean logout
    time.sleep(1)
    
    # Redirect to Login/Register page using the correct file path
    st.switch_page(r"pages/01LoginRegister.py")
def main():
    st.title("Logging Out")
    # Inform user about logout process
    st.info("Logging you out...")
    # Call logout function
    handle_logout()
if __name__ == "__main__":
    main()
