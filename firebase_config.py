# firebase_config.py
import pyrebase

firebaseConfig = {
    "apiKey": "your-real-client-id",
    "authDomain": "your-real-client-id",
    "databaseURL": "your-real-client-id",  # Provide if using Realtime DB; else leave blank
    "projectId": "your-real-client-id",
    "storageBucket": "your-real-client-id",
    "messagingSenderId": "your-real-client-id",
    "appId": "your-real-client-id"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# Firebase Auth
auth = firebase.auth()

# If using Realtime Database
db = firebase.database()
