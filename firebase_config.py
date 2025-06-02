# firebase_config.py
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyD5l6ZiWTMDqoA7zqzSrqgQ_7uMCJAW9sM",
    "authDomain": "medscore-assist.firebaseapp.com",
    "databaseURL": "https://medscore-assist-default-rtdb.asia-southeast1.firebasedatabase.app/",  # Provide if using Realtime DB; else leave blank
    "projectId": "medscore-assist",
    "storageBucket": "medscore-assist.firebasestorage.app",
    "messagingSenderId": "207857923434",
    "appId": "1:207857923434:web:a89b72e7ce45e36f9d2113"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# Firebase Auth
auth = firebase.auth()

# If using Realtime Database
db = firebase.database()
