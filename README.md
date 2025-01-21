# Gym Management System

A comprehensive Gym Management System built using **Python** and **Django**, designed to streamline and automate various operations in gym management. This project offers robust features for handling memberships, equipment, and personalized diet plans.

## Features

- **Membership Management**: Add, view, and manage gym members efficiently.
- **Equipment Tracking**: Maintain records of gym equipment, including availability and maintenance.
- **Personalized Diet Plans**: Generate AI-based diet plans for members based on their input (height, weight, sex, etc.).
- **Enquiry Handling**: Manage and respond to member and visitor queries seamlessly.
- **User Authentication**: Secure login and registration system for members and admin.
- **Responsive UI**: A clean and user-friendly interface for easy navigation.

## Technologies Used

- **Backend**: Python, Django Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default), with support for other databases
- **AI Integration**: AI-based diet plan generation using ChatGPT-like models

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.7 or above
- pip (Python package manager)
- Django 4.x

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/gym-management-system.git
   cd gym-management-system
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
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

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## File Structure

```
gym-management-system/
├── gym_management/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── members/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── equipment/
│   ├── models.py
│   ├── views.py
│   └── templates/
├── templates/
│   ├── base.html
│   ├── member_home.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── manage.py
├── requirements.txt
└── README.md
```

## Key Functionalities

### Membership Management
- Add, update, and delete member details.
- View a detailed list of active members.

### Equipment Management
- Add and track gym equipment.
- Update the status of equipment (e.g., available, under maintenance).

### Personalized Diet Plan
- Members input their details (height, weight, goals, etc.).
- The system generates a personalized diet plan using AI.

### Enquiry System
- Handle queries submitted by members or visitors.
- Admin can view and respond to queries from the dashboard.

## Screenshots



## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## Contact

For any inquiries or support:

- **Email**: your.email@example.com
- **GitHub**: RaghuRahMathur(https://github.com/yourusername)

---

Thank you for using the Gym Management System! 💪
