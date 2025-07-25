# ClinicFlow – A Role-Based Clinic Management System

ClinicFlow is a full-stack web application for managing clinic operations with user roles such as patient, doctor, receptionist, and admin. It’s built using Flask, Flask-JWT-Extended for authentication, SQLite for storage, and plain HTML/CSS/JS for the frontend.

## Features

- **Role-Based Access Control**
  - Patient: Register, login, book appointments.
 
![Screenshot 2025-06-24 222948](https://github.com/user-attachments/assets/8eb8b417-6389-45d8-abc4-88c4eadc30f3)


  - Doctor: View their scheduled appointments.
  - Receptionist: View and confirm pending appointments.

![Screenshot 2025-06-24 224032](https://github.com/user-attachments/assets/15651a93-8b33-457d-9c9b-c150fef91f3d)


  - Admin: Create/manage doctors and receptionists, view/delete all appointments.

![Screenshot 2025-06-24 223110](https://github.com/user-attachments/assets/1d10135d-0309-41e2-a58f-48b7e434c48f)


- **Authentication**
  - Secure login and role validation using JWT.

- **Appointment Management**
  - Patients can book appointments with selected doctors.
  - Receptionist confirms pending appointments.
  - Admin can delete or view all appointments.

## Tech Stack

- Backend: Flask, Flask-JWT-Extended, SQLAlchemy
- Frontend: HTML, CSS, JavaScript
- Database: SQLite

## Installation

#### 1. Clone the repo:

```
git clone https://github.com/hemantkumarlearning/clinicflow.git
cd clinicflow
```

#### 2. Create and activate a virtual environment:

```
cd backend
python -m venv env
env/Scripts/activate
```

#### 3. Install dependencies:

```
pip install -r requirements.txt
```

#### 4. Set the environment variable:

```
SECRET_KEY=YOUR-SECRET KEY
JWT_SECRET_KEY=YOUR-JWT-SECRET-KEY
DATABASE_URL=sqlite:///db.sqlite3
```

#### 5. Run the app:

```
python app.py
```

Now you can use postman for testing or Go to frontend folder and open or use vscode Go live to open register.html on browser 

```
cd .
cd frontend
```



