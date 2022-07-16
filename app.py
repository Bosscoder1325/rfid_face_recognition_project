from flask import Flask
import pyrebase

app = Flask(__name__)

config = {
  "apiKey": "AIzaSyAZoAADcMtseOtxeAh6jLcpH3or24ZhL8c",
  "authDomain": "rfid-aaea6.firebaseapp.com",
  "databaseURL": "https://rfid-aaea6-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "rfid-aaea6",
  "storageBucket": "rfid-aaea6.appspot.com",
  "messagingSenderId": "621829893183",
  "appId": "1:621829893183:web:e04119660c08c0c44a1c8a",
  "measurementId": "G-3GT9ED7KXE"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return db.get("PresentList")


# main driver function
if __name__ == '__main__':
    app.run()
