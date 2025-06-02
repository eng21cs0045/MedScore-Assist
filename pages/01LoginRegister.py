import streamlit as st
import requests
from urllib.parse import urlencode, quote_plus
import pyrebase
import json
import time
import secrets
import string

# Page configuration with sidebar permanently hidden
st.set_page_config(
    page_title="MedScore Assist - Login",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling and permanently hiding sidebar
st.markdown("""
<style>
    /* Hide sidebar permanently */
    .css-1d391kg, .st-emotion-cache-1d391kg,
    [data-testid="stSidebar"], .css-1lcbmhc,
    .st-emotion-cache-1lcbmhc, .sidebar .sidebar-content,
    section[data-testid="stSidebar"] {
        display: none !important;
        width: 0 !important;
        min-width: 0 !important;
        max-width: 0 !important;
    }
    
    /* Remove sidebar toggle button */
    .css-14xtw13, .st-emotion-cache-14xtw13,
    button[kind="header"] {
        display: none !important;
    }
    
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    /* Block container styling */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
        max-width: 500px !important;
        margin: 0 auto !important;
        width: 100% !important;
    }
    
    /* Remove default Streamlit spacing */
    .element-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .stMarkdown {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: 700;
        margin: 0.5rem 0 0 0 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .sub-header {
        text-align: center;
        color: #00008B !important;
        font-size: 1.5rem;
        margin: 0 0 0.5rem 0 !important;
        font-weight: 400;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    /* Tab container styling */
    .stTabs {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem !important;
        border-radius: 15px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        max-width: 400px !important;
        width: 400px !important;
        margin: 0 auto !important;
        box-sizing: border-box !important;
    }
    
    /* Tab list styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background-color: #f8f9fa;
        padding: 6px;
        border-radius: 10px;
        margin: 0 0 1.5rem 0 !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        padding: 0px 20px;
        background-color: transparent;
        border-radius: 8px;
        color: #6c757d;
        font-weight: 500;
        border: none;
        transition: all 0.3s ease;
        flex: 1;
        justify-content: center;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Tab panel content styling */
    .stTabs [data-baseweb="tab-panel"] {
        padding: 0 !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    /* Form styling */
    .stTabs .stForm {
        width: 100% !important;
        box-sizing: border-box !important;
        max-width: 100% !important;
        margin: 0 auto !important;
    }
    
    /* Input field styling */
    .stTabs .stTextInput {
        width: 100% !important;
        margin-bottom: 1.2rem !important;
        box-sizing: border-box !important;
    }
    
    .stTabs .stTextInput > div {
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    .stTabs .stTextInput > div > div {
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    .stTabs .stTextInput > div > div > input {
        background-color: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 14px 18px;
        font-size: 15px;
        transition: all 0.3s ease;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    .stTabs .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        background-color: white;
        outline: none;
    }
    
    /* Input labels */
    .stTabs .stTextInput label {
        color: #495057 !important;
        font-weight: 600 !important;
        margin-bottom: 6px !important;
        display: block !important;
        font-size: 15px !important;
    }
    
    /* Button styling */
    .stTabs .stButton {
        width: 100% !important;
        margin-top: 1.2rem !important;
        box-sizing: border-box !important;
    }
    
    .stTabs .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 14px 28px;
        font-size: 15px;
        font-weight: 600;
        width: 100% !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        box-sizing: border-box !important;
    }
    
    .stTabs .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Section headers */
    .stTabs h3 {
        color: #333 !important;
        font-size: 1.6rem !important;
        font-weight: 600 !important;
        margin: 0 0 1.5rem 0 !important;
        text-align: center !important;
    }
    
    /* Google button styling */
    .google-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 14px 20px;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        background-color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none !important;
        width: 100%;
        margin-top: 1.2rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        box-sizing: border-box;
    }
    
    .google-btn:hover {
        border-color: #667eea;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .google-btn img {
        margin-right: 10px;
    }
    
    .google-btn span {
        color: #5f6368;
        font-family: 'Roboto', Arial, sans-serif;
        font-size: 15px;
        font-weight: 500;
    }
    
    /* Divider styling */
    .divider {
        text-align: center;
        margin: 1.5rem 0;
        position: relative;
        color: #6c757d;
        font-size: 13px;
        font-weight: 500;
    }
    
    .divider:before {
        content: '';
        position: absolute;
        top: 50%;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, #e9ecef 20%, #e9ecef 80%, transparent);
    }
    
    .divider span {
        background: white;
        padding: 0 1rem;
    }
    
    /* Success/Error message styling */
    .stSuccess, .stError {
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    /* Debug info styling - HIDDEN IN PRODUCTION */
    .debug-info {
        display: none !important; /* Change to 'block' for debugging */
        background: rgba(255,255,255,0.9);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-family: monospace;
        font-size: 12px;
        border-left: 4px solid #007bff;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .block-container {
            max-width: calc(100vw - 2rem) !important;
            margin: 0 1rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        
        .stTabs {
            margin: 0 !important;
            padding: 1.5rem !important;
            max-width: calc(100vw - 2rem) !important;
            width: calc(100vw - 2rem) !important;
            border-radius: 12px;
        }
        
        .main-header {
            font-size: 2.2rem;
            margin: 0.3rem 0 0.2rem 0 !important;
        }
        
        .sub-header {
            margin: 0 0 0.8rem 0 !important;
        }
    }
    
    /* Hide Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Google OAuth Configuration
GOOGLE_CLIENT_ID = "207857923434-3iaocbdg54hdfi7bqnrnjmi6rocjt8al.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:8501"  # Simplified redirect URI
FIREBASE_API_KEY = "AIzaSyD5l6ZiWTMDqoA7zqzSrqgQ_7uMCJAW9sM"

# Initialize Firebase with Pyrebase
firebaseConfig = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": "medscore-assist.firebaseapp.com",
    "databaseURL": "https://medscore-assist-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "projectId": "medscore-assist",
    "storageBucket": "medscore-assist.firebasestorage.app",
    "messagingSenderId": "207857923434",
    "appId": "1:207857923434:web:a89b72e7ce45e36f9d2113"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# Function to generate a secure random password
def generate_secure_password(length=12):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()_-+=<>?"
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Function to generate Google OAuth URL
def get_google_auth_url(mode="login"):
    scope = "openid email profile"
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": scope,
        "access_type": "offline",
        "prompt": "consent",
        "state": mode
    }
    encoded_params = urlencode(params, quote_via=quote_plus)
    return f"https://accounts.google.com/o/oauth2/v2/auth?{encoded_params}"

# Function to exchange authorization code for tokens
def exchange_code_for_token(code):
    if not code:
        return None, None
    
    token_url = "https://oauth2.googleapis.com/token"
    
    payload = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    
    try:
        response = requests.post(token_url, data=payload)
        
        if response.status_code != 200:
            return None, None
            
        token_data = response.json()
        return token_data.get("id_token"), token_data.get("access_token")
    except Exception:
        return None, None

# Function to get email from Google access token
def get_email_from_google_token(access_token):
    if not access_token:
        return None
        
    try:
        user_info_url = "https://www.googleapis.com/oauth2/v3/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        
        response = requests.get(user_info_url, headers=headers)
        
        if response.status_code != 200:
            return None
            
        user_info = response.json()
        return user_info.get("email")
    except Exception:
        return None

# FIXED: Improved email existence check
def email_exists(email):
    """Check if email exists in Firebase Auth using a more reliable method"""
    if not email:
        return False
    
    try:
        # Use Firebase Auth REST API to check if email exists
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:createAuthUri?key={FIREBASE_API_KEY}"
        payload = {
            "identifier": email,
            "continueUri": "http://localhost:8501"
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            # If 'registered' key exists and is True, email is registered
            return data.get('registered', False)
        else:
            # Fallback: try the old method
            return email_exists_fallback(email)
            
    except Exception as e:
        print(f"Error checking email existence: {e}")
        # Fallback method
        return email_exists_fallback(email)

def email_exists_fallback(email):
    """Fallback method to check email existence"""
    try:
        # Try to sign in with a dummy password
        auth.sign_in_with_email_and_password(email, "dummy_password_that_wont_work_123456")
        return True
    except Exception as e:
        error_message = str(e).upper()
        if "INVALID_PASSWORD" in error_message or "WRONG_PASSWORD" in error_message:
            return True  # Email exists but password is wrong
        elif "EMAIL_NOT_FOUND" in error_message or "USER_NOT_FOUND" in error_message:
            return False  # Email doesn't exist
        elif "INVALID_LOGIN_CREDENTIALS" in error_message:
            # This could mean either email doesn't exist OR password is wrong
            # Let's be more conservative and assume it exists
            return True
        else:
            print(f"Unexpected error in email_exists_fallback: {error_message}")
            return False

# FIXED: Improved login function with better error handling
def attempt_direct_login(email, password):
    """Attempt to login with email and password"""
    if not email or not password:
        return None, "Please enter both email and password."
    
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user, None
    except Exception as e:
        error_message = str(e).upper()
        
        if "INVALID_PASSWORD" in error_message or "WRONG_PASSWORD" in error_message:
            return None, "Invalid password. Please try again."
        elif "EMAIL_NOT_FOUND" in error_message or "USER_NOT_FOUND" in error_message:
            return None, "Email is not registered. Please register first."
        elif "INVALID_LOGIN_CREDENTIALS" in error_message:
            return None, "Invalid email or password. Please check your credentials."
        elif "TOO_MANY_ATTEMPTS_TRY_LATER" in error_message:
            return None, "Too many failed attempts. Please try again later."
        elif "USER_DISABLED" in error_message:
            return None, "This account has been disabled. Please contact support."
        else:
            print(f"Login error: {error_message}")
            return None, "Login failed. Please try again."

# Function to register new user
def register_new_user(email, password):
    if not email or not password:
        return None, "Please provide both email and password."
    
    try:
        # Check if email already exists first
        if email_exists(email):
            return None, "Email already registered. Please login instead."
        
        user = auth.create_user_with_email_and_password(email, password)
        
        # Store additional user data
        sanitized_email = email.replace('.', ',')
        user_data = {
            'email': email,
            'has_password': True,
            'user_id': user['localId'],
            'created_at': time.time()
        }
        db.child("users").child(sanitized_email).set(user_data)
        
        return user, None
    except Exception as e:
        error_message = str(e).upper()
        if "EMAIL_EXISTS" in error_message:
            return None, "Email already registered. Please login instead."
        elif "WEAK_PASSWORD" in error_message:
            return None, "Password is too weak. Please use at least 6 characters."
        elif "INVALID_EMAIL" in error_message:
            return None, "Invalid email format. Please enter a valid email."
        else:
            print(f"Registration error: {error_message}")
            return None, "Registration failed. Please try again."

# Function to clear session state
def clear_session_state():
    """Clear all session state except essential keys"""
    keys_to_keep = ['oauth_state']
    for key in list(st.session_state.keys()):
        if key not in keys_to_keep:
            del st.session_state[key]

# Function to initialize session state
def initialize_session_state():
    """Initialize session state with default values"""
    if "oauth_state" not in st.session_state:
        st.session_state.oauth_state = "initial"
    if "user" not in st.session_state:
        st.session_state.user = None
    if "error_message" not in st.session_state:
        st.session_state.error_message = None

# Function to display debug info (hidden in production)
def display_debug_info():
    """Display debug information for development"""
    debug_info = {
        "oauth_state": st.session_state.get("oauth_state", "None"),
        "user_logged_in": st.session_state.get("user") is not None,
        "error_message": st.session_state.get("error_message", "None"),
        "query_params": dict(st.query_params)
    }
    
    st.markdown(f"""
    <div class="debug-info">
        <strong>Debug Info:</strong><br>
        {json.dumps(debug_info, indent=2)}
    </div>
    """, unsafe_allow_html=True)

# Main Function
def main():
    # Initialize session state
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">MEDSCORE ASSIST</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your Medical Assessment Companion</p>', unsafe_allow_html=True)
    
    # Display debug info (hidden by CSS in production)
    display_debug_info()
    
    # Check if user is already logged in
    if st.session_state.user is not None:
        user_email = st.session_state.user.get('email', 'Unknown')
        st.success(f"✅ Welcome back, {user_email}!")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Go to Dashboard", use_container_width=True):
                # Navigate to landing page
                st.switch_page("pages/02LandingPage.py")
        with col2:
            if st.button("🚪 Logout", use_container_width=True):
                clear_session_state()
                st.query_params.clear()
                st.rerun()
        return
    
    # Display error message if present
    if st.session_state.error_message:
        st.error(st.session_state.error_message)
        # Clear error after displaying
        st.session_state.error_message = None
    
    # Handle Google OAuth callback
    auth_code = st.query_params.get("code", "")
    auth_mode = st.query_params.get("state", "login")
    
    if auth_code and st.session_state.oauth_state == "initial":
        st.session_state.oauth_state = "processing"
        
        try:
            id_token, access_token = exchange_code_for_token(auth_code)
            st.query_params.clear()
            
            if access_token and id_token:
                email = get_email_from_google_token(access_token)
                
                if email:
                    if auth_mode == "register":
                        if email_exists(email):
                            st.session_state.error_message = f"Email {email} is already registered. Please login instead."
                        else:
                            # Create new user with Google
                            password = generate_secure_password()
                            user, error = register_new_user(email, password)
                            if user:
                                st.session_state.user = user
                                st.success("✅ Registration successful! You are now logged in.")
                            else:
                                st.session_state.error_message = error
                    else:  # login mode
                        if not email_exists(email):
                            st.session_state.error_message = f"Email {email} is not registered. Please register first."
                        else:
                            # For existing Google users, we need to handle authentication differently
                            # This is a simplified approach - in production, you'd want proper Google Firebase integration
                            st.session_state.user = {"email": email, "localId": "google_user"}
                            st.success("✅ Login successful!")
                else:
                    st.session_state.error_message = "Could not retrieve email from Google account."
            else:
                st.session_state.error_message = "Authentication failed. Please try again."
                
        except Exception as e:
            st.session_state.error_message = f"Authentication error: {str(e)}"
        
        st.session_state.oauth_state = "completed"
        st.rerun()
    
    # Main login/register interface
    if st.session_state.oauth_state in ["initial", "completed"]:
        tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])
        
        with tab1:
            with st.form("login_form", clear_on_submit=False):
                st.markdown("### Welcome Back!")
                email = st.text_input("📧 Email Address", placeholder="Enter your email")
                password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
                login_submitted = st.form_submit_button("🚀 Log In")

            if login_submitted:
                if email and password:
                    with st.spinner("Logging you in..."):
                        user, error_message = attempt_direct_login(email, password)
                    
                    if user:
                        st.session_state.user = user
                        st.success("✅ Login successful!")
                        time.sleep(1)  # Brief pause to show success message
                        st.rerun()
                    else:
                        st.session_state.error_message = error_message
                        st.rerun()
                else:
                    st.session_state.error_message = "Please enter both email and password."
                    st.rerun()

            # Google Login Button
            st.markdown('<div class="divider"><span>or continue with</span></div>', unsafe_allow_html=True)
            
            login_auth_url = get_google_auth_url(mode="login")
            google_login_html = f'''
                <a href="{login_auth_url}" target="_self" class="google-btn">
                    <img src="https://developers.google.com/identity/images/g-logo.png"
                        alt="Google Logo" width="20" height="20">
                    <span>Continue with Google</span>
                </a>
            '''
            st.markdown(google_login_html, unsafe_allow_html=True)

        with tab2:
            with st.form("register_form", clear_on_submit=False):
                st.markdown("### Create Your Account")
                new_email = st.text_input("📧 Email Address", placeholder="Enter your email")
                new_password = st.text_input("🔒 Password", type="password", placeholder="Create a strong password")
                confirm_password = st.text_input("🔒 Confirm Password", type="password", placeholder="Confirm your password")
                register_submitted = st.form_submit_button("🎉 Create Account")

            if register_submitted:
                if not new_email or not new_password or not confirm_password:
                    st.session_state.error_message = "Please fill in all required fields."
                    st.rerun()
                elif new_password != confirm_password:
                    st.session_state.error_message = "Passwords do not match."
                    st.rerun()
                elif len(new_password) < 6:
                    st.session_state.error_message = "Password must be at least 6 characters long."
                    st.rerun()
                else:
                    with st.spinner("Creating your account..."):
                        user, error_message = register_new_user(new_email, new_password)
                    
                    if user:
                        st.success("✅ Registration successful! Please log in now.")
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.session_state.error_message = error_message
                        st.rerun()

            # Google Register Button
            st.markdown('<div class="divider"><span>or sign up with</span></div>', unsafe_allow_html=True)
            
            register_auth_url = get_google_auth_url(mode="register")
            google_register_html = f'''
                <a href="{register_auth_url}" target="_self" class="google-btn">
                    <img src="https://developers.google.com/identity/images/g-logo.png"
                        alt="Google Logo" width="20" height="20">
                    <span>Sign up with Google</span>
                </a>
            '''
            st.markdown(google_register_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
