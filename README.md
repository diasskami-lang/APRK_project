A full-stack intelligent web system for managing and recognizing government employees of Kazakhstan.

This project combines:

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Node.js + Express.js
* **Database:** PostgreSQL
* **AI Recognition API:** FastAPI + InsightFace
* **Authentication:** Admin / User roles

---

# 📌 Project Overview

# Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript (Vanilla)

## Backend

* Node.js
* Express.js

## Database

* PostgreSQL

## AI / Recognition

* Python
* FastAPI
* InsightFace
* OpenCV
* NumPy

---

# 📂 Project Structure

```bash
project/
│── frontend/
│   ├── index.html
│   ├── main.html
│   └── script.js
│
│── backend/
│   ├── server.js
│   ├── db.js
│   └── package.json
│
│── ai/
│   ├── api.py
│   └── main.py
│
└── README.md
```

---

#  Roles

## Admin

Can:

* Login as administrator
* Add new employee
* Edit employee data
* Delete employee
* Upload photo
* Use recognition system

## User

Can:

* Login as user
* Search employee
* View table
* Use recognition system

Cannot:

* Edit data
* Delete data
* Add new employee

---

# PostgreSQL Setup

Create database:

```sql
CREATE DATABASE gov_system;
```

Create table:

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    fullname TEXT NOT NULL,
    photo TEXT,
    position TEXT,
    ministry TEXT,
    start_date DATE,
    end_date DATE
);
```

---

# ⚙️ Backend Setup

## Install packages

```bash
npm install express pg cors body-parser
```

## Run server

```bash
node server.js
```

Server runs on:

```bash
http://localhost:3000
```

---

#  AI Setup

## Install Python packages

```bash
pip install fastapi uvicorn insightface opencv-python numpy python-multipart
```

## Run API

```bash
uvicorn api:app --reload
```

Runs on:

```bash
http://localhost:8000
```

---

# Face Recognition Logic

System uses **InsightFace embeddings**.

Process:

1. Upload image
2. Detect face
3. Generate embedding vector
4. Compare with database faces
5. Return most similar employee

Example response:

```json
{
  "name": "Dias Nurgaliyev",
  "accuracy": "93.2%"
}
```

---

# 🌐 Frontend Pages

## index.html

Beautiful login page.

Supports:

* Admin login
* User login
* Role based redirect

---

## main.html

Dashboard page:

* Employee table
* Search bar
* Add employee button
* Edit button
* Delete button
* Recognize person button

Buttons hidden automatically for normal users.

---

# Demo Credentials

## Admin

```text
username: admin
password: 1234
```

## User

```text
username: user
password: 1234
```

---

# Example Screens

## Login Page

Modern glassmorphism UI.

## Main Dashboard

Professional table with controls.

## AI Recognition

Upload photo → detect person.

---

# 🔥 Run Full Project

## Terminal 1

```bash
node server.js
```

## Terminal 2

```bash
uvicorn api:app --reload
```

## Browser

Open:

```bash
index.html
```


