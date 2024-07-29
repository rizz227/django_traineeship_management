Django Student Management System
This project is a comprehensive Student Management System developed using Python with the Django framework, designed for educational purposes.

If you find this project valuable, please consider starring the repository to show your support.

Features
Admin Users
Overview Dashboards: View summary charts for student performance, staff performance, and course statistics.
Staff Management: Add, update, and delete staff members.
Student Management: Add, update, and delete student records.
Course Management: Add, update, and delete courses.
Subject Management: Add, update, and delete subjects.
Session Management: Add, update, and delete academic sessions.
Attendance Monitoring: View and manage student attendance.
Staff/Teachers
Summary Charts: Access charts related to students, subjects, and leave status.
Attendance Management: Record and update student attendance.
Results Management: Add and update student results.
Feedback Submission: Provide feedback to the Head of Department (HOD).
Students
Summary Charts: View charts related to attendance, subjects, and leave status.
Attendance View: Check personal attendance records.
Results View: Access academic results.
Feedback Submission: Send feedback to the Head of Department (HOD).
Installation and Setup
Prerequisites
Git: Version control system

Download Git
Python: Latest version

Download Python
Pip: Python package manager

Pip Installation Guide
Installation Steps
Create a Directory for the Project

bash
Copier le code
mkdir django-student-management-system
cd django-student-management-system
Set Up a Virtual Environment

Install Virtual Environment:
bash
Copier le code
pip install virtualenv
Create the Virtual Environment:
For Windows:
bash
Copier le code
python -m venv venv
For macOS/Linux:
bash
Copier le code
python3 -m venv venv
Activate the Virtual Environment:
For Windows:
bash
Copier le code
venv\Scripts\activate
For macOS/Linux:
bash
Copier le code
source venv/bin/activate
Clone the Repository

bash
Copier le code
git clone https://github.com/yourusername/django-student-management-system.git
cd django-student-management-system
Install Project Dependencies

bash
Copier le code
pip install -r requirements.txt
Configure Allowed Hosts

Open settings.py in your project.
Update the ALLOWED_HOSTS setting:
python
Copier le code
ALLOWED_HOSTS = ['*']
Run the Development Server

For Windows:
bash
Copier le code
python manage.py runserver
For macOS/Linux:
bash
Copier le code
python3 manage.py runserver
Create a Superuser

bash
Copier le code
python manage.py createsuperuser
Follow the prompts to set up the superuser credentials.
Default Credentials for Testing:

HOD/SuperAdmin
Email: admin@gmail.com
Password: admin
Staff
Email: staff@gmail.com
Password: staff
Student
Email: student@gmail.com
Password: student
License
This project is licensed under the MIT License. See the LICENSE file for details.

Copyright © 2022 @ritikbanger

Permission is granted, free of charge, to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:

Include the copyright notice and permission notice in all copies or substantial portions of the Software.
The Software is provided "as is", without warranty of any kind. The authors or copyright holders are not liable for any claims, damages, or other liabilities.
