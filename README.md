﻿# Student Management Website

A comprehensive student management system built with **Python Django**, **HTML**, **Bootstrap**, and **SQL**. This web application simplifies the process of managing student data, providing features for administrators, teachers, and students.

## Features

- **Admin Panel**:
  - Manage students, teachers, and classes.
  - Generate reports and track student performance.
- **Teacher Dashboard**:
  - View assigned classes and student details.
  - Add and update grades and attendance.
- **Student Portal**:
  - Access grades, attendance, and personal information.
  - Update profile information.
- **Responsive Design**:
  - Built with Bootstrap for a user-friendly interface on all devices.

## Technologies Used

- **Backend**: Python (Django Framework)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQL (SQLite / MySQL / PostgreSQL)
- **Other**: Django ORM for database operations

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/student-management.git
   cd student-management
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Update the database configuration in `settings.py`.
   - Apply migrations:
     ```bash
     python manage.py migrate
     ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. **Admin Login**:
   - Default admin credentials:
     - Username: `admin`
     - Password: `admin123` (change this after the first login).

2. **Teacher and Student Accounts**:
   - Register accounts or add them via the admin panel.

3. **Managing Data**:
   - Use the admin panel to add, update, or delete student and teacher records.

## Screenshots

### Home Page
##![Home Page](Uploading Soon)

### Admin Dashboard
##![Admin Dashboard](Uploading Soon)

### Student Profile
##![Student Profile](Uploading Soon)

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact:

- **Name**: [Aakash S Hari](https://www.linkedin.com/in/aakash-s-2209a1257/)
- **Email**: aakashpc123@gmail.com
- **GitHub**: [Aakash S](https://github.com/aakash10802)

