# fullstack-books

## Overview
This project is a full-stack web application for managing a database of books. It includes a front-end interface for users to view, add, edit, and delete books, and a back-end with a RESTful API to interact with the SQLite database.

## Installation
To set up the project locally, follow these steps:
1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies with `pip install -r requirements.txt`.
4. Set up the environment variables in `.flaskenv` and `instance/config.py`.
5. Initialize the database with `flask db upgrade`.
6. Run the application with `flask run`.

## Usage
Once the application is running, navigate to `localhost:5000` in your web browser to access the book database interface. You can view the list of books, add new books, edit existing books, or delete books from the database.

## Deployment
The application is deployed on PythonAnywhere. For updates, push the changes to the repository and pull them on the PythonAnywhere environment. Restart the web app to apply the changes.

## Features
- Browse and search books
- View detailed book information
- Add and edit books
- User reviews and ratings
- Wishlist and favorites
- Responsive design
- User authentication and profile management
- Accessibility features

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python with Flask
- Database: SQLite
- ORM: SQLAlchemy
- Deployment: PythonAnywhere

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
