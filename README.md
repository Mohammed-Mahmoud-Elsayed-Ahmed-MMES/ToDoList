# To-Do List Application

## Introduction
This is a full-stack web application for managing tasks in a To-Do list. Users can create, read, update, and delete (CRUD) tasks. The backend is built using Django and Django REST Framework to provide a REST API, and the frontend is implemented with HTML, CSS, and JavaScript.

## Project Structure
todo_project/
├── .dockerignore               # Ignores files during Docker build (e.g., db.sqlite3)
├── .gitignore                  # Ignores files for Git (e.g., env/, db.sqlite3)
├── Dockerfile                  # Docker configuration for building the app
├── manage.py                   # Django management script
├── README.md                   # Project documentation
├── db.sqlite3                  # SQLite database (local development)
├── ToDoList/                   # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── static/
│       └── admin/
│           └── css/
│               ├── autocomplete.css
│               ├── base.css
│               ├── changelists.css
│               ├── dark_mode.css
│               ├── dashboard.css
│               └── login.css
├── crud/                       # Django app for to-do list functionality
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── 0001_initial.py
│       ├── 0002_remove_item_completed_at_remove_item_created_at_and_more.py
│       ├── 0003_item_completed_at_item_created_at_item_updated_at.py
│       ├── 0004_remove_item_completed_at_remove_item_updated_at.py
│       └── __init__.py
├── staticfiles/                # Collected static files (generated, not tracked in Git)
│   ├── rest_framework/
│   │   └── js/
│   │       ├── default.js
│   │       ├── default.js.gz
│   │       ├── jquery-3.7.1.min.js
│   │       ├── prettify-min.js
│   │       └── load-ajax-form.js
│   └── staticfiles.json
└── templates/                  # HTML templates
    ├── base.html
    └── crud/
        └── index.html


## Features
- **CRUD operations**: Add, view, edit, and delete tasks.
- **Switch between table and card views**: Users can choose how they want to display tasks for better visibility.
- **RESTful API**: Utilizes Django REST Framework to expose the backend API.
- **Responsive UI**: The frontend adapts to various screen sizes, including mobile devices.
- **Enhanced UI/UX**: Includes hover effects and intuitive form layouts tailored for ease of use.
- **Preloader**: An animated preloader for a better user experience while the content loads.
- **CSRF protection**: Security layer implemented in all forms and API requests.

## Core Work and Challenges
- **Backend Development with Django REST Framework**: One of the core challenges was setting up and connecting the Django backend with the frontend to ensure that the data flowed seamlessly between them. Designing the API and handling complex request-response cycles while maintaining data integrity was key to this project.
  
- **Handling CRUD Operations**: Implementing create, read, update, and delete (CRUD) operations on the frontend with real-time interaction from the backend was tricky. Coordinating the Django models and serializers with JavaScript's fetch API for dynamic updates was challenging but rewarding.

- **Dynamic Data Fetching with JavaScript**: Another challenge was fetching data from the backend and rendering it dynamically on the frontend using JavaScript's promises and `fetch()`. The handling of asynchronous data and integrating it into the UI required careful management of the frontend-backend interaction, especially with the new table and card view options.

- **Cross-Site Request Forgery (CSRF) Protection**: Managing CSRF tokens when performing API requests from JavaScript was a challenge. It required careful setup to ensure secure data transactions while maintaining a seamless user experience.

- **Responsive Design**: Ensuring the design worked smoothly across all devices, especially for forms and tables, involved troubleshooting CSS for responsiveness, including media queries and adjusting layouts for mobile devices.

## API Endpoints
- **GET /api/items/**: Retrieve all tasks
- **POST /api/items/**: Add a new task
- **GET /api/items/{id}/**: Retrieve a specific task
- **PUT /api/items/{id}/**: Update a task
- **DELETE /api/items/{id}/**: Delete a task

## Installation & Setup
### Prerequisites
- **Python** 3.8+
- Django 4.x
- Django REST Framework
- **Docker**: Required to run the project in a containerized environment.
- **Git**: To clone the repository.

## Setup and Running Locally

### 1. Clone the Repository
Clone the project from GitHub:

```bash
git clone https://github.com/Mohammed-Mahmoud-Elsayed-Ahmed-MMES/ToDoList.git
cd ToDoList
```

### 2. Create a Virtual Environment
Set up a virtual environment to manage dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages (you may need to create a `requirements.txt` if it doesn't exist):

```bash
pip install django djangorestframework
```

If a `requirements.txt` file exists, install dependencies from it:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
Set up the database by applying migrations:

```bash
python manage.py migrate
```

### 5. Collect Static Files
Collect static files for the admin interface and REST framework:

```bash
python manage.py collectstatic --noinput
```

### 6. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

- Open your browser and go to `http://localhost:8000/` to see the to-do list app.
- Access the admin interface at `http://localhost:8000/admin/` (create a superuser with `python manage.py createsuperuser` to log in).
- Access the REST API at `http://localhost:8000/api/` (if configured in `urls.py`).

## Running with Docker

### 1. Build the Docker Image
Ensure Docker is installed and running. Build the Docker image using the provided `Dockerfile`:

```bash
docker build -t todo-list .
```

### 2. Run the Docker Container
Run the container, mapping the container's port 8000 to your local port 8000:

```bash
docker run -d -p 8000:8000 --name todo-list-container todo-list
```

- The `-d` flag runs the container in detached mode.
- The `-p 8000:8000` flag maps port 8000 on your machine to port 8000 in the container.

### 3. Apply Migrations in the Container
If the database needs to be set up, exec into the container and apply migrations:

```bash
docker exec -it todo-list-container python manage.py migrate
```

### 4. Collect Static Files in the Container
Collect static files inside the container:

```bash
docker exec -it todo-list-container python manage.py collectstatic --noinput
```

### 5. Access the App
- Open your browser and go to `http://localhost:8000/` to see the to-do list app.
- Access the admin interface at `http://localhost:8000/admin/`.
- Access the REST API at `http://localhost:8000/api/` (if configured).

### 6. Stop the Container
To stop the running container:

```bash
docker stop todo-list-container
```

## Additional Notes

- **Database**: The project uses SQLite (`db.sqlite3`) for development. For production, consider switching to a more robust database like PostgreSQL by updating `settings.py`.
- **Static Files**: The `staticfiles/` directory is generated by `collectstatic` and should not be tracked in Git. Ensure `.gitignore` includes `staticfiles/`.
- **Deployment**: The app is deployed on a hosting platform at `https://to-do-list-f102be19b0d3.hosted.ghaymah.systems`. The `Dockerfile` and `.dockerignore` are used for containerized deployment.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.
