KPA Backend Assignment – API Development
This is a Django-based backend project implementing two APIs as per the assignment requirements. It connects to a PostgreSQL database and is integrated with the Flutter frontend (partially tested).

✅ 1. Bogie Checksheet Submission API
Endpoint:  http://127.0.0.1:8000/api/forms/bogie-checksheet/
Purpose: Submits a filled bogie checksheet form to the backend.
Functionality Covered:
Accepts structured bogie inspection data
Validates fields and nested JSON objects
Stores data in PostgreSQL
Type: POST
Features: Nested JSON, structured form data, PostgreSQL integration

✅ 2.Wheel Specifications API
Endpoint: GET /api/forms/wheel-specifications/
Purpose: Retrieve wheel specification records from PostgreSQL.
Method: GET
Filters Supported (optional):
formNumber
submittedBy
submittedDate

Example Request:
http://127.0.0.1:8000/api/forms/wheel-specifications/?formNumber=WHEEL-2025-002&submittedBy=user_id_789&submittedDate=2025-07-18



📁 Cloning & Running the Project

git clone https://github.com/CHEMAN456/KPA.git
cd KPA

📦 Install Dependencies
pip install -r requirements.txt

🛠 Database Setup
python manage.py makemigrations
python manage.py migrate

 Run Server
 
python manage.py runserver
Server will be live at: http://127.0.0.1:8000

⚠️ Flutter Frontend Integration

Login API tested and working ✅
Data submission partially integrated (Bogie + Wheel forms)
Full integration was attempted, but due to CORS/local limitations, some Flutter API calls did not complete successfully.
