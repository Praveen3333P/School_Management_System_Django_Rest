# 📌 School Management System API

A simple **Django Rest Framework (DRF)** API to manage students, teachers, and courses.

## 🚀 Features
- CRUD operations for **Students, Teachers, and Courses**  
- Implements **Function-Based Views (FBV), Class-Based Views (CBV), ViewSets, Generic Views, and Mixins**   

## 🛠️ Setup  
1. **Clone the repository**  
   ```sh
   git clone https://github.com/Praveen3333P/School_Management_System_Django_Rest.git
   ```
2. **Create & activate a virtual environment**  
   ```sh
   python -m venv venv 
   venv\Scripts\activate    
   ```
3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations & start the server**  
   ```sh
   python manage.py makemigrations api  
   python manage.py migrate  
   python manage.py runserver  
   ```
5. **Access API at** `http://127.0.0.1:8000/api/`

## 📌 API Endpoints  
| Endpoint            | Method           | Description                 |
|---------------------|------------------|-----------------------------|
| `/api/students/`    | GET, POST        | List all students / Create a new student |
| `/api/students/{id}`| GET, PUT, DELETE | Retrieve, update, or delete a student |
| `/api/teachers/`    | GET, POST        | List all teachers / Create a new teacher |
| `/api/courses/`     | GET, POST        | List all courses / Create a new course |


