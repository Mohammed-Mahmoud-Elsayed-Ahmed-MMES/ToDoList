FROM python:3.11-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "--workers", "3", "ToDoList.wsgi:application"]

# ----------------------------------------------------------------

# FROM python:3.11-slim

# # Update package lists and upgrade existing packages
# RUN apt-get update && apt-get upgrade -y

# # Install python3-dev for Python development headers and gcc for compilation
# RUN apt-get install -y python3-dev gcc && rm -rf /var/lib/apt/lists/*

# # Set the working directory
# WORKDIR /app

# # Copy requirements.txt and install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire project directory
# COPY . .

# # Collect static files for Django
# RUN python manage.py collectstatic --noinput

# # Run migrations (only if using a managed database)
# # Uncomment this if you set DATABASE_URL in the deployment platform
# # RUN python manage.py migrate

# # Expose port 8000 for the web server
# EXPOSE 8000

# # Run Gunicorn to serve the Django app
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--timeout", "120", "--workers", "3", "ToDoList.wsgi:application"]

#   Will Keeping EXPOSE 8000 80 443 and the Current CMD Cause Errors?
    #     No, it won’t cause an error. Exposing multiple ports is valid syntax and won’t break the build or runtime behavior.
    #     However, it’s unnecessary in your case because:
    #     Your app (via Gunicorn) only listens on port 8000.
    #     The hosting platform (Ghaymah Systems) handles external HTTP/HTTPS traffic (on ports 80/443) and forwards it to your container’s port 8000 (as configured in the platform’s settings: port 8000, public).
    #     Exposing ports 80 and 443 in the Dockerfile has no effect since your app isn’t listening on those ports.

# 2. CMD ["gunicorn", "--bind", "0.0.0.0:8000", "0.0.0.0:443", "0.0.0.0:80", "ToDoList.wsgi:application"]
    # Will It Cause an Error?:
    #     Yes, it will cause an error. Gunicorn will interpret 0.0.0.0:443 and 0.0.0.0:80 as additional arguments, not additional bind addresses, leading to a failure to start.


# -------------------------------------------------------------------------------

# # Use an official Python runtime as the base image
# FROM python:3.11-slim

# # Set working directory in the container
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     gcc \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements.txt and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the entire project directory
# COPY . .

# # Collect static files
# RUN python manage.py collectstatic --noinput

# # Expose port 8000 for Gunicorn
# EXPOSE 8000

# # Run Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ToDoList.wsgi:application"]