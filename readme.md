# Personal Blog Project

Welcome to my **Personal Blog Project** created with Django!

## Overview

This project is a simple yet powerful blogging platform that allows users to:

- Sign up and log in to their accounts.
- View blog posts created by other users on the home page without logging in.
- Create, update, and delete their own blog posts once logged in.
- Update their profile information.
- Reset their password if forgotten.
- Like and comment on blog posts.
- View blog posts specifically created by them on their profile page.


## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite
- **Authentication**: Django's built-in authentication system
- **Password Reset**: Django's built-in password reset functionality
- **Icons**: Font Awesome for like and comment functionality

## Getting Started

To run the project on your local machine, follow these steps:

1. Clone the repository to your local machine.
2. Open the project in your favorite code editor.
3. Create and activate a virtual environment.
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the command to make migrations:
    ```bash
    python manage.py makemigrations
    ```
6. Apply the migrations:
    ```bash
    python manage.py migrate
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```
8. Open your browser and navigate to the URL displayed in the terminal where the project is running.
9. You can now view and interact with the blog project on your local machine.
