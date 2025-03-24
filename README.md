<<<<<<< HEAD
# smart-attendance
نظام تسجيل الحضور باستخدام Flask وGoogle Sheets
=======
# Smart Attendance System

Flask backend to receive check-ins from users and log them to Google Sheets based on geolocation.

## Setup

1. Add your `credentials.json` file (Google Service Account).
2. Create a Google Sheet named "SmartAttendance" and share it with the service account email.
3. Deploy using Render.

## Endpoint

- `POST /attendance`  
  Payload:
  ```json
  {
    "name": "John Doe",
    "latitude": 30.0444,
    "longitude": 31.2357,
    "timestamp": "2025-03-24T12:00:00Z"
  }
  ```
>>>>>>> 7d36452 (Initial commit)
