Gym Management System

A comprehensive Gym Management System built using **Python** and **Django**, designed to streamline and automate gym operations such as membership management, equipment tracking, and personalized diet plans.

## Features

- **Membership Management**: Add, view, and manage gym members effectively.
- **Equipment Tracking**: Track gym equipment availability and maintenance status.
- **User Authentication**: Secure login system for members and administrators.
- **Enquiry Handling**: Manage member queries through an intuitive interface.
- **Responsive UI**: A user-friendly and visually appealing design.

## Technologies Used

- **Backend**: Python, Django Framework
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Hosting**: Vercel (for deployment)
- **Other Tools**: `.env` for environment variables, `vercel.json` for deployment configuration

## File Structure

```
Gym_Management_System/
├── gym/
│   ├── static/
│   │   └── script/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── utils.py
│   └── views.py
├── GymManagementDjango/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── static/
├── .env
├── .gitattributes
├── .gitignore
├── buildfiles.sh
├── db.sqlite3
├── manage.py
├── requirements.txt
└── vercel.json
```

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/gym-management-system.git
   cd gym-management-system
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\\Scripts\\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Deployment

This project is configured for deployment on **Vercel**. Use the included `vercel.json` and `buildfiles.sh` for setup.

## Key Functionalities

### Membership Management
- Add, update, and delete member records.
- View a list of active gym members.

### Equipment Tracking
- Maintain a detailed list of gym equipment.
- Update equipment availability and maintenance records.

### Personalized Diet Plan
- Generate AI-based diet plans based on user input.

### Enquiry System
- Handle and respond to user queries through the admin panel.

## Screenshots
- index page : ![image](https://github.com/user-attachments/assets/88d1be37-ad23-42a3-94ef-d9d90b7d7297)
- Why choose Us : ![image](https://github.com/user-attachments/assets/05f750cd-9b1e-4c57-ab92-ed210bd741b9)
- testimonials : ![image](https://github.com/user-attachments/assets/60999c39-d9f6-45d6-bec6-3fed7e37bfc4)
- Our classes : ![image](https://github.com/user-attachments/assets/602e70e5-052f-4d94-abce-8030c85229e5)
- annonuncements : ![image](https://github.com/user-attachments/assets/982d264a-b9f6-4f42-82df-5684673d5ac4)
- Admin Login : ![image](https://github.com/user-attachments/assets/7d7ca37d-28fc-4fe4-9680-09c902d0dcca)
- member login : ![image](https://github.com/user-attachments/assets/90910d7d-6666-4dd2-8c88-5217eb694051)
- member plan : ![image](https://github.com/user-attachments/assets/904d79f8-4d7b-4d72-aee7-d491590e65d2)
- contact page : ![image](https://github.com/user-attachments/assets/15d109dc-d9b2-4948-ac25-82c75c0090e5)
- admin dashboard : ![image](https://github.com/user-attachments/assets/f5800126-2567-4146-a83f-88b9debce8cb)
- member dashboard : ![image](https://github.com/user-attachments/assets/685cc94d-fdef-4617-9355-7c368c889df9)

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For inquiries or support, contact:
- **Email**: raghuu715@gmailcom
- **GitHub**: RaghuRajMathur(https://github.com/RaghuRajMathur)

---

Let me know if you'd like to modify anything!
