import streamlit as st
from PIL import Image

# ============ Set Page Config ============
st.set_page_config(
    page_title="Medscore Assist",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============ Apply Custom CSS ============
def local_css():
    st.markdown("""
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
            
            /* === GLOBAL === */
            html, body {
                font-family: 'Poppins', 'Helvetica Neue', sans-serif;
                font-size: 18px;
                color: #333333;
                line-height: 1.6;
            }

            .block-container {
                padding-top: 4rem;
                padding-bottom: 2rem;
                padding-left: 4rem;
                padding-right: 4rem;
            }

            h1, h2, h3 {
                font-weight: 700;
                color: #00ae99;
            }

            p {
                font-size: 18px;
                margin-bottom: 1em;
            }

            /* === HEADER === */
            .medscore-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding-bottom: 10px;
                margin-bottom: 30px;
                border-bottom: 1px solid #eee;
            }

            .medscore-logo {
                height: 60px;
            }

            .login-button {
                font-size: 16px;
                font-weight: bold;
                padding: 10px 20px;
                background-color: #00ae99;
                color: white;
                border: none;
                border-radius: 25px;
                cursor: pointer;
                text-decoration: none;
                width: 200px;
                height: 50px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .login-button:hover {
                background-color: #008f7a;
            }

            .login-button img {
                margin-right: 10px;
                width: 20px;
                height: 20px;
            }

            .section-title {
                font-size: 28px;
                font-weight: 600;
                margin-top: 2rem;
                color: #00ae99;
            }

            .how-it-works-icons {
                text-align: center;
                margin-top: 30px;
            }

            .testimonial {
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin: 10px;
                font-style: italic;
                font-size: 17px;
                height: 100%;
            }

            /* === FOOTER === */
            .footer-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                gap: 20px;
                margin-top: 40px;
            }

            .footer-block {
                flex: 1 1 200px;
                min-width: 200px;
                background-color: #f9f9f9;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }

            .footer-block h3 {
                font-size: 20px;
                color: #2c3e50;
                margin-bottom: 0.5em;
                border-bottom: 2px solid #4CAF50;
                display: inline-block;
                padding-bottom: 0.2em;
            }

            .footer-link {
                display: block;
                margin: 0.5em 0;
                padding: 0.5em;
                border-radius: 8px;
                background-color: #e8f5e9;
                color: #2c3e50 !important;
                text-decoration: none;
                font-weight: 500;
                transition: all 0.2s ease;
                font-size: 16px;
            }

            .footer-link:hover {
                background-color: #c8e6c9;
                transform: scale(1.05);
                text-decoration: none;
                color: #000000 !important;
            }

            /* Social Icons */
            .footer-block a img {
                vertical-align: middle;
                margin-right: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

local_css()

# ============ Header ============
col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    logo = Image.open("mda.jpg")
    st.image(logo, width=180)
with col2:
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>WELCOME TO MEDSCORE ASSIST</h1>", unsafe_allow_html=True)
with col3:
    st.markdown('<a href="/LoginRegister" class="login-button"> 👤 Login / Register</a>', unsafe_allow_html=True)

# ============ Welcome Section ============
# ============ Welcome Section ============
st.markdown("""
    <div style="text-align: center; padding: 30px 20px; background-color: #f1fdfc; border-radius: 15px;">
        <h2 style="color: #00ae99; font-size: 36px; font-weight: 700; margin-bottom: 10px;">
            Your Personal Health Risk Navigator
        </h2>
        <p style="font-size: 22px; color: #333333; line-height: 1.8; max-width: 900px; margin: auto;">
            <strong>Medscore Assist</strong> is your intelligent health companion. Using advanced AI and real-world clinical data,
            it helps you detect early warning signs of heart disease, diabetes, and more—long before symptoms appear.
            <br><br>
            Whether you're tracking your health progress, managing a condition, or simply staying proactive,
            Medscore delivers personalized insights and actionable steps tailored to your unique profile.
            <br><br>
            🌿 <em>Prevention starts here. Take control of your health, confidently and smartly—with Medscore Assist.</em>
        </p>
    </div>
""", unsafe_allow_html=True)


# ============ How It Works Section ============
st.markdown('<div class="section-title"></div>', unsafe_allow_html=True)
how_it_works_image = Image.open("Howitworks.png")

left, center, right = st.columns([1, 2, 1])
with center:
    st.image(how_it_works_image, width=900)

# ============ Why Medscore ============
# ============ Why Medscore ============
st.markdown("""
    <div style="text-align: center; margin-top: 40px; margin-bottom: 20px;">
        <h2 style="color: #00ae99; font-size: 34px; font-weight: 700;">Why Medscore?</h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="font-size: 20px; line-height: 1.8; color: #333333;">
    <strong>Medscore Assist</strong> is an advanced health risk assessment tool that leverages AI to provide accurate and personalized risk predictions for conditions like heart disease, hypertension, and obesity. 
    By analyzing both clinical data and lifestyle factors such as age, diet, physical activity, and genetics, Medscore gives a comprehensive view of your health. 
    <br><br>
    The system offers easy-to-understand insights, along with actionable recommendations to help you proactively manage your health. Medscore is designed with an intuitive and user-friendly interface, making it accessible to everyone.
    <br><br>
    Your privacy is our priority—Medscore ensures fast, secure, and confidential handling of your personal health data. In addition to risk predictions, Medscore provides tailored health plans and real-time monitoring to help you stay on track.
    <br><br>
    With clinically validated models, Medscore offers reliable predictions and empowers users to take charge of their health journey with confidence.
</div>
""", unsafe_allow_html=True)


# ============ Testimonials ============
st.markdown('<div class="section-title">What Our Customers Say</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("""
        <div class="testimonial">
            “Medscore Assist has completely transformed the way I track my health. It’s incredibly easy to use, and the AI-driven insights have helped me understand my health risks better. The ability to get personalized recommendations has been invaluable. A must-have for anyone who wants to stay ahead of their health!” – Adarsh Jaiswal.
        </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
        <div class="testimonial">
            “Medscore Assist alerted me to early signs of hypertension that I wouldn’t have noticed otherwise. The detailed risk prediction and preventive suggestions helped me make crucial lifestyle changes, and I now feel more in control of my health. I highly recommend it to anyone looking to take proactive steps for better health.” – Hayley Kenner.
        </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
        <div class="testimonial">
            “I absolutely love the clean, user-friendly design of Medscore Assist. It not only gives me clear and actionable health insights but also helps me track my progress. The ability to see the results in real time and get tailored recommendations makes a huge difference. The results are accurate and truly helpful—definitely a tool I will continue using!” – Daniel R.
        </div>
    """, unsafe_allow_html=True)

# ============ Footer: Locations, Clients, Partners ============
st.markdown("""
<div class="footer-container">
  <div class="footer-block">
    <h3>📍 Locations</h3>
    <a href="https://www.google.com/maps/place/Bangalore" target="_blank" class="footer-link">Bangalore</a>
    <a href="https://www.google.com/maps/place/Chennai" target="_blank" class="footer-link">Chennai</a>
    <a href="https://www.google.com/maps/place/Delhi" target="_blank" class="footer-link">Delhi</a>
  </div>

  <div class="footer-block">
    <h3>🤝 Clients</h3>
    <a href="/clients_corporate" class="footer-link">Corporate</a>
    <a href="/clients_ngo" class="footer-link">NGO</a>
    <a href="/clients_rwa" class="footer-link">RWA</a>
  </div>

   <div class="footer-block">
    <h3>🏥 Partners</h3>
    <a href="/partners_hospitals" class="footer-link">Hospitals</a>
    <a href="/partners_chemists" class="footer-link">Chemists</a>
    <a href="/partners_nurses" class="footer-link">Nurses</a>
    <a href="/partners_doctors" class="footer-link">Doctors</a>
  </div>

  <div class="footer-block">
    <h3>Follow us on</h3>
    <a href="https://www.instagram.com" target="_blank">
      <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="24" height="24"> Instagram
    </a><br>
    <a href="https://www.linkedin.com/in/yourprofile" target="_blank">
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="24" height="24"> LinkedIn
    </a><br>
    <a href="https://twitter.com/yourprofile" target="_blank">
      <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/x.svg" width="24" height="24"> X
    </a><br><br>
    &copy; 2025 Medscore Assist
  </div>

</div>
""", unsafe_allow_html=True)
