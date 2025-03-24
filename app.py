from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os

app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
client = gspread.authorize(creds)

# افتح الشيت بالاسم
sheet = client.open("SmartAttendance").sheet1  # اسم الشيت من جوجل

@app.route('/attendance', methods=['POST'])
def attendance():
    data = request.get_json()

    try:
        name = data['name']
        lat = data['latitude']
        lng = data['longitude']
        timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        sheet.append_row([name, timestamp, lat, lng])

        return jsonify({"success": True, "message": "Recorded successfully."}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "✅ Smart Attendance API is running!", 200

if __name__ == '__main__':
    app.run(debug=True)
