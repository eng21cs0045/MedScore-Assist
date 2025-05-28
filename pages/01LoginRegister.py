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
    
    /* Adjust main content area */
    .main .block-container, .st-emotion-cache-z5fcl4 {
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }
    
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    /* CRITICAL: Remove all default Streamlit spacing */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0.5rem !important;
        max-width: 500px !important;  /* REDUCED FROM 1200px */
        margin: 0 auto !important;
        width: 100% !important;
    }
    
    /* AGGRESSIVE spacing removal - target all possible Streamlit containers */
    .element-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .stMarkdown {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Target ALL Streamlit spacing classes - ENHANCED */
    .css-1y4p8pa, .st-emotion-cache-1y4p8pa,
    .css-ocqkz7, .st-emotion-cache-ocqkz7,
    .css-16idsys, .st-emotion-cache-16idsys,
    .css-1wbqy5l, .st-emotion-cache-1wbqy5l,
    .css-1d391kg, .st-emotion-cache-1d391kg,
    .css-12oz5g7, .st-emotion-cache-12oz5g7,
    .css-1y0tads, .st-emotion-cache-1y0tads,
    .css-k1vhr4, .st-emotion-cache-k1vhr4,
    .css-1629p8f, .st-emotion-cache-1629p8f,
    .css-10trblm, .st-emotion-cache-10trblm,
    .css-16huue1, .st-emotion-cache-16huue1 {
        margin: 0 !important;
        padding: 0 !important;
        gap: 0 !important;
    }
    
    /* Force tight spacing on containers */
    .stContainer, .stContainer > div {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Remove gaps between consecutive elements - ENHANCED */
    .stMarkdown + .stTabs,
    .stMarkdown + .stContainer,
    .stContainer + .stTabs,
    .stMarkdown + .stMarkdown,
    div[data-testid="element-container"] + div[data-testid="element-container"] {
        margin-top: 0 !important;
    }
    
    /* SPECIFIC FIX: Target the exact spacing issue between header and tabs */
    .stTabs {
        margin-top: 0 !important;
        padding-top: 0 !important;
        max-width: 100% !important;
        width: 100% !important;
    }
    
    /* Target any empty div containers that might be causing spacing */
    div:empty,
    .stMarkdown:empty,
    .element-container:empty {
        display: none !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Header styling with tight spacing */
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
        color: #00008B !important;  /* Teal */
        font-size: 1.5rem;
        margin: 0 0 0.5rem 0 !important;
        font-weight: 400;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);  /* Added text shadow for better readability */
    }
    
    /* SMALLER WHITE CONTAINER: Reduced tab styling */
    .stTabs {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem !important;  /* REDUCED FROM 3rem */
        border-radius: 15px;  /* REDUCED FROM 20px */
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);  /* REDUCED shadow */
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        max-width: 400px !important;  /* REDUCED FROM 100% */
        width: 400px !important;  /* FIXED WIDTH - SMALLER */
        margin: 0 auto !important;  /* CENTER THE SMALLER BOX */
        box-sizing: border-box !important;
    }
    
    /* FIXED: Tab list styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;  /* REDUCED FROM 8px */
        background-color: #f8f9fa;
        padding: 6px;  /* REDUCED FROM 8px */
        border-radius: 10px;  /* REDUCED FROM 12px */
        margin: 0 0 1.5rem 0 !important;  /* REDUCED FROM 2rem */
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 45px;  /* REDUCED FROM 50px */
        padding: 0px 20px;  /* REDUCED FROM 24px */
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
    
    /* FIXED: Tab panel content styling */
    .stTabs [data-baseweb="tab-panel"] {
        padding: 0 !important;
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    /* SMALLER FORM: Form container within tabs */
    .stTabs .stForm {
        width: 100% !important;
        box-sizing: border-box !important;
        max-width: 100% !important;  /* FILL THE SMALLER CONTAINER */
        margin: 0 auto !important;
    }
    
    /* FIXED: Input field styling with proper containment */
    .stTabs .stTextInput {
        width: 100% !important;
        margin-bottom: 1.2rem !important;  /* REDUCED FROM 1.5rem */
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
        border-radius: 10px;  /* REDUCED FROM 12px */
        padding: 14px 18px;  /* REDUCED FROM 16px 20px */
        font-size: 15px;  /* REDUCED FROM 16px */
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
    
    /* FIXED: Input labels */
    .stTabs .stTextInput label {
        color: #495057 !important;
        font-weight: 600 !important;
        margin-bottom: 6px !important;  /* REDUCED FROM 8px */
        display: block !important;
        font-size: 15px !important;  /* REDUCED FROM 16px */
    }
    
    /* SMALLER BUTTON: Button styling with proper containment */
    .stTabs .stButton {
        width: 100% !important;
        margin-top: 1.2rem !important;  /* REDUCED FROM 1.5rem */
        box-sizing: border-box !important;
    }
    
    .stTabs .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;  /* REDUCED FROM 12px */
        padding: 14px 28px;  /* REDUCED FROM 16px 32px */
        font-size: 15px;  /* REDUCED FROM 16px */
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
    
    /* SMALLER HEADERS: Section headers within tabs */
    .stTabs h3 {
        color: #333 !important;
        font-size: 1.6rem !important;  /* REDUCED FROM 1.8rem */
        font-weight: 600 !important;
        margin: 0 0 1.5rem 0 !important;  /* REDUCED FROM 2rem */
        text-align: center !important;
    }
    
    /* SMALLER Google button styling */
    .google-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 14px 20px;  /* REDUCED FROM 16px 24px */
        border: 2px solid #e9ecef;
        border-radius: 10px;  /* REDUCED FROM 12px */
        background-color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none !important;
        width: 100%;
        margin-top: 1.2rem;  /* REDUCED FROM 1.5rem */
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        box-sizing: border-box;
    }
    
    .google-btn:hover {
        border-color: #667eea;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    .google-btn img {
        margin-right: 10px;  /* REDUCED FROM 12px */
    }
    
    .google-btn span {
        color: #5f6368;
        font-family: 'Roboto', Arial, sans-serif;
        font-size: 15px;  /* REDUCED FROM 16px */
        font-weight: 500;
    }
    
    /* Divider styling */
    .divider {
        text-align: center;
        margin: 1.5rem 0;  /* REDUCED FROM 2rem */
        position: relative;
        color: #6c757d;
        font-size: 13px;  /* REDUCED FROM 14px */
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
        border-radius: 10px;  /* REDUCED FROM 12px */
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    /* NUCLEAR OPTION: Remove all possible margins and paddings from Streamlit */
    [data-testid="element-container"],
    [data-testid="block-container"],
    .element-container,
    .block-container {
        max-width: 500px !important;  /* REDUCED FROM 1200px */
        margin: 0 auto !important;
        width: 100% !important;
    }
    
    /* Specific targeting for the problematic white space */
    .main > div:first-child {
        padding-top: 0 !important;
        margin-top: 0 !important;
        max-width: 500px !important;  /* REDUCED FROM 1200px */
        margin-left: auto !important;
        margin-right: auto !important;
        width: 100% !important;
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
            padding: 1.5rem !important;  /* REDUCED FROM 2rem */
            max-width: calc(100vw - 2rem) !important;
            width: calc(100vw - 2rem) !important;
            border-radius: 12px;
        }
        
        .stTabs .stForm {
            max-width: 100% !important;
        }
        
        .main-header {
            font-size: 2.2rem;  /* REDUCED FROM 2.5rem */
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
GOOGLE_CLIENT_ID = "your-real-client-id"
GOOGLE_CLIENT_SECRET = "your-real-client-id"
REDIRECT_URI = "http://localhost:8501/LoginRegister"
FIREBASE_API_KEY = "your-real-client-id"

# Initialize Firebase with Pyrebase
firebaseConfig = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": "your-real-client-id",
    "databaseURL": "your-real-client-id",
    "storageBucket": "your-real-client-id",
    "messagingSenderId": "your-real-client-id",
    "appId": "your-real-client-id"
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
    scope = "openid email profile https://www.googleapis.com/auth/userinfo.email"
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": scope,
        "access_type": "offline",
        "prompt": "consent",
        "include_granted_scopes": "true",
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
        
        if "refresh_token" in token_data:
            st.session_state["refresh_token"] = token_data["refresh_token"]
            
        return token_data.get("id_token"), token_data.get("access_token")
    except Exception as e:
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
    except Exception as e:
        return None

# Improved function to reliably check if email exists in Firebase
def email_exists(email):
    if not email:
        return False
        
    try:
        url = f"https://identitytoolkit.googleapis.com/v1/accounts:createAuthUri?key={FIREBASE_API_KEY}"
        payload = {
            "identifier": email,
            "continueUri": REDIRECT_URI
        }
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("registered", False)
    except Exception:
        pass
        
    try:
        auth.sign_in_with_email_and_password(email, "ThisIsADeliberatelyWrongPassword123!@#")
        return True
    except Exception as e:
        error_message = str(e)
        if "INVALID_PASSWORD" in error_message:
            return True
        elif "EMAIL_NOT_FOUND" in error_message or "INVALID_LOGIN_CREDENTIALS" in error_message:
            return False
        
    return False

# Function to check if user is registered with email/password
def is_email_password_user(email):
    try:
        user_data_ref = db.child("users").child(email.replace('.', ','))
        user_data = user_data_ref.get().val()
        return user_data and 'has_password' in user_data and user_data['has_password']
    except Exception:
        return False

# Function to link Google sign-in with email/password
def link_google_with_email_password(email, user_id):
    try:
        password = generate_secure_password()
        
        sanitized_email = email.replace('.', ',')
        user_data = {
            'email': email,
            'has_password': True,
            'password': password,
            'user_id': user_id
        }
        
        db.child("users").child(sanitized_email).set(user_data)
        
        return password
    except Exception as e:
        st.error(f"Error linking account: {str(e)}")
        return None

# Function to sign in with Firebase using Google ID token
def firebase_sign_in_with_google(id_token, email, mode="login"):
    if not id_token or not email:
        return None

    try:
        firebase_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithIdp?key={FIREBASE_API_KEY}"
        payload = {
            "postBody": f"id_token={id_token}&providerId=google.com",
            "requestUri": REDIRECT_URI,
            "returnIdpCredential": True,
            "returnSecureToken": True
        }
        
        response = requests.post(firebase_url, json=payload)
        response_json = response.json()
        
        if response.status_code != 200:
            return None
            
        if "email" not in response_json:
            return None
            
        is_new_user = response_json.get("isNewUser", False)
        
        if mode == "register" and not is_new_user:
            return {"error": "already_registered", "email": email}
            
        if mode == "login" and is_new_user:
            return {"error": "not_registered", "email": email}
        
        if mode == "register" and is_new_user:
            user_id = response_json.get("localId")
            password = link_google_with_email_password(email, user_id)
            if password:
                response_json["generated_password"] = password
            
        return response_json
    except Exception as e:
        return None

# Function to attempt direct login with email and password
def attempt_direct_login(email, password):
    if not email or not password:
        return None, "Please enter both email and password."
    
    try:
        sanitized_email = email.replace('.', ',')
        user_data = db.child("users").child(sanitized_email).get().val()
        
        if user_data and user_data.get('has_password', False):
            if user_data.get('password') == password:
                user = auth.sign_in_with_email_and_password(email, password)
                return user, None
            else:
                return None, "Invalid password. Please try again."
        
        user = auth.sign_in_with_email_and_password(email, password)
        return user, None
    except Exception as e:
        error_message = str(e)
        if "INVALID_PASSWORD" in error_message:
            return None, "Invalid password. Please try again."
        elif "INVALID_LOGIN_CREDENTIALS" in error_message or "EMAIL_NOT_FOUND" in error_message:
            sanitized_email = email.replace('.', ',')
            user_data = db.child("users").child(sanitized_email).get().val()
            
            if user_data:
                return None, "This account was registered with Google. Please use 'Login with Google' button."
            else:
                return None, "Email is not registered. Please register first."
        else:
            return None, f"Login failed: {error_message}"

# Function to log out the user
def handle_logout():
    keys_to_keep = []
    
    for key in list(st.session_state.keys()):
        if key not in keys_to_keep:
            del st.session_state[key]
    
    st.query_params.clear()
    st.rerun()

# Main Function
def main():
    # Header with tight spacing
    st.markdown('<h1 class="main-header">MEDSCORE ASSIST</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your Medical Assessment Companion</p>', unsafe_allow_html=True)
    
    # Initialize session state
    if "oauth_state" not in st.session_state:
        st.session_state.oauth_state = "initial"
        
    if "current_tab" not in st.session_state:
        st.session_state.current_tab = "login"
        
    if "error_message" not in st.session_state:
        st.session_state.error_message = None

    # User is already logged in - redirect to Landing Page
    if "user" in st.session_state and not isinstance(st.session_state["user"], dict) or \
    "user" in st.session_state and isinstance(st.session_state["user"], dict) and "error" not in st.session_state["user"]:
        
        user_email = st.session_state['user'].get('email', '')
        st.success(f"✅ Welcome back, logged in as {user_email}!")
        
        time.sleep(3)
        st.switch_page(r"C:\Users\My pc\Dropbox\PC\Desktop\MP_authentication_21stMay_Final\pages\02LandingPage.py")

    # Display error if present
    if "error_message" in st.session_state and st.session_state.error_message:
        error_placeholder = st.empty()
        error_placeholder.error(st.session_state.error_message)
        time.sleep(3)
        error_placeholder.empty()
        st.session_state.error_message = None
        st.rerun()

    # Get state (mode) and code from query parameters
    has_auth_code = "code" in st.query_params
    auth_code = st.query_params.get("code", "") if has_auth_code else ""
    auth_mode = st.query_params.get("state", "login")
    
    # Process Google OAuth callback only once
    if has_auth_code and st.session_state.oauth_state == "initial":
        st.session_state.oauth_state = "processing"
        
        try:
            id_token, access_token = exchange_code_for_token(auth_code)
            
            st.query_params.clear()
            
            if access_token and id_token:
                email = get_email_from_google_token(access_token)
                
                if email:
                    firebase_user = firebase_sign_in_with_google(id_token, email, auth_mode)
                    if firebase_user:
                        if "error" in firebase_user:
                            if firebase_user["error"] == "already_registered":
                                st.session_state.error_message = f"Email {firebase_user['email']} is already registered. Please login instead."
                                st.session_state.current_tab = "login"
                            elif firebase_user["error"] == "not_registered":
                                st.session_state.error_message = f"Email {firebase_user['email']} is not registered. Please register first."
                                st.session_state.current_tab = "register"
                            st.session_state.oauth_state = "failed"
                            st.rerun()
                        else:
                            st.session_state["user"] = firebase_user
                            
                            if "generated_password" in firebase_user:
                                st.session_state["generated_password"] = firebase_user["generated_password"]
                            
                            st.session_state.oauth_state = "completed"
                            
                            if auth_mode == "register":
                                st.success("✅ Registration successful! Please log in now.")
                                st.session_state.current_tab = "login"
                            else:
                                st.success("✅ Login successful!")
                                st.rerun()
                    else:
                        st.session_state.error_message = "Firebase authentication failed. Please try again."
                        st.session_state.oauth_state = "failed"
                else:
                    st.session_state.error_message = "Could not retrieve email from Google account."
                    st.session_state.oauth_state = "failed"
            else:
                st.session_state.error_message = "Could not obtain tokens from Google."
                st.session_state.oauth_state = "failed"
            
        except Exception as e:
            st.session_state.error_message = f"Authentication error: {str(e)}"
            st.session_state.oauth_state = "failed"
    
    # Reset state if authentication failed
    if st.session_state.oauth_state == "failed":
        if st.button("🔄 Try Again"):
            st.session_state.oauth_state = "initial"
            st.query_params.clear()
            st.session_state.error_message = None
            st.rerun()

    # Main form container
    if st.session_state.oauth_state == "initial":
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        # Use tabs for switching between login and register
        tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])
        
        with tab1:
            with st.form("login_form", clear_on_submit=False):
                st.markdown("### Welcome Back!")
                email = st.text_input("📧 Email Address", placeholder="Enter your email")
                password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
                login_submitted = st.form_submit_button("🚀 Log In")

            if login_submitted and email and password:
                user, error_message = attempt_direct_login(email, password)
                
                if user:
                    st.session_state["user"] = user
                    st.success("✅ Login successful!")
                    time.sleep(1)
                    st.rerun()
                elif error_message:
                    st.session_state.error_message = error_message
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
                if not new_email or not new_password:
                    st.session_state.error_message = "Please fill in all required fields."
                    st.rerun()
                elif new_password != confirm_password:
                    st.session_state.error_message = "Passwords do not match."
                    st.rerun()
                else:
                    try:
                        if email_exists(new_email):
                            st.session_state.error_message = "Email already registered. Please login instead."
                            st.rerun()
                        else:
                            user = auth.create_user_with_email_and_password(new_email, new_password)
                            
                            sanitized_email = new_email.replace('.', ',')
                            user_data = {
                                'email': new_email,
                                'has_password': True,
                                'password': new_password,
                                'user_id': user['localId']
                            }
                            db.child("users").child(sanitized_email).set(user_data)
                            
                            st.success("✅ Registration successful! Please log in now.")
                            st.session_state.current_tab = "login"
                            time.sleep(2)
                            st.rerun()
                    except Exception as e:
                        error_message = str(e)
                        if "EMAIL_EXISTS" in error_message:
                            st.session_state.error_message = "Email already registered. Please login instead."
                        else:
                            st.session_state.error_message = f"Registration failed: {error_message}"
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
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()