from pathlib import Path # Imports Path for file path handling
import os # Imports os for environment variables and file paths
import dj_database_url # Imports dj_database_url for database URL parsing (used in production)

BASE_DIR = Path(__file__).resolve().parent.parent # Sets the base directory for the project (used for file paths)

# Security Settings: Loads sensitive values from environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-$&6d+m+$cum(+6n4voo(7r$3k!^+b11%f3^5ex2cr12a!-xiz#') # Loads SECRET_KEY from env (affects app security, default for local dev)
DEBUG = os.getenv('DEBUG', 'True') == 'True' # Loads DEBUG from env (affects error display, True for local dev)

# Allowed Hosts: Defines which hosts can access the app
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1,to-do-list-f102be19b0d3.hosted.ghaymah.systems,to-do-list-def7dea78b26.hosted.ghaymah.systems,to-do-list.com,www.to-do-list.com').split(',') # Loads hosts from env (affects request handling)

INSTALLED_APPS = [ # Defines the installed Django apps
    'django.contrib.admin', # Admin interface
    'django.contrib.auth', # Authentication system
    'django.contrib.contenttypes', # Content types framework
    'django.contrib.sessions', # Session management
    'django.contrib.messages', # Messaging framework
    'django.contrib.staticfiles', # Static file handling
    'rest_framework', # Django REST Framework (used for API, though simplified in views.py)
    'crud', # Custom app for to-do list functionality (affects urls.py, views.py)
    'corsheaders', # CORS headers for cross-origin requests (affects middleware)
]

MIDDLEWARE = [ # Defines the middleware stack
    'django.middleware.security.SecurityMiddleware', # Security enhancements
    'whitenoise.middleware.WhiteNoiseMiddleware', # Static file serving (affects static files in production)
    'django.contrib.sessions.middleware.SessionMiddleware', # Session handling
    'corsheaders.middleware.CorsMiddleware', # CORS handling (affects cross-origin requests from main.js)
    'django.middleware.common.CommonMiddleware', # Common middleware (e.g., append slash)
    'django.middleware.csrf.CsrfViewMiddleware', # CSRF protection (affects POST/PUT/DELETE requests in main.js)
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware', # Messaging middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking protection
]

CORS_ALLOWED_ORIGINS = [ # Defines allowed origins for CORS
    "https://to-do-list-f102be19b0d3.hosted.ghaymah.systems", # Deployed domain
    "https://to-do-list-def7dea78b26.hosted.ghaymah.systems", # Deployed domain
    "http://localhost:8000", # Local development
    "http://127.0.0.1:8000", # Local development (added for broader compatibility)
    "https://to-do-list.com", # Custom domain
    "https://www.to-do-list.com", # Custom domain with www
]

ROOT_URLCONF = 'ToDoList.urls' # Specifies the root URL configuration (affects urls.py)

TEMPLATES = [ # Defines template settings
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Uses Django templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Includes templates directory (affects index.html, base.html)
        'APP_DIRS': True, # Enables app-specific templates (affects crud/index.html)
        'OPTIONS': {
            'context_processors': [ # Context processors for templates
                'django.template.context_processors.debug', # Debug context
                'django.template.context_processors.request', # Request context
                'django.contrib.auth.context_processors.auth', # Authentication context
                'django.contrib.messages.context_processors.messages', # Messages context
            ],
        },
    },
]

WSGI_APPLICATION = 'ToDoList.wsgi.application' # Specifies the WSGI application (used by Gunicorn)

# Database Settings: Configures the database
DATABASES = { # Defines the database configuration
    'default': { # Default database
        'ENGINE': 'django.db.backends.sqlite3', # Uses SQLite for local dev
        'NAME': BASE_DIR / 'db.sqlite3', # Sets the database file path (affects database operations)
    }
}

if 'DATABASE_URL' in os.environ: # Overrides with DATABASE_URL if present (for production)
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True) # Configures production database (affects database operations)

# Password Validators: Defines password validation rules
AUTH_PASSWORD_VALIDATORS = [ # Password validation settings
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}, # Checks similarity to user attributes
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'}, # Enforces minimum length
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'}, # Prevents common passwords
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}, # Prevents numeric-only passwords
]

# Internationalization Settings
LANGUAGE_CODE = 'en-us' # Sets the language to English (affects templates)
TIME_ZONE = 'UTC' # Sets the timezone to UTC (affects timestamps in database)
USE_I18N = True # Enables internationalization (affects templates)
USE_TZ = True # Enables timezone support (affects timestamps in database)

# Static Files Settings
STATIC_URL = '/static/' # Sets the URL for static files (affects static file serving)
STATICFILES_DIRS = [BASE_DIR / 'static'] # Sets the directory for static files (affects main.js, styles.css)
STATIC_ROOT = BASE_DIR / 'staticfiles' # Sets the directory for collected static files (affects collectstatic)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Uses WhiteNoise for static file serving (affects production)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Sets the default primary key type (affects database models)
APPEND_SLASH = True # Automatically appends slashes to URLs (affects URL routing)

# Security Settings for Production
SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'False') == 'True' # Redirects HTTP to HTTPS in production (affects request handling)
SESSION_COOKIE_SECURE = True # Ensures session cookies are secure (affects session security in production)
CSRF_COOKIE_SECURE = True # Ensures CSRF cookies are secure (affects CSRF protection in production)

# ------------------------------------------------------------------------

# from pathlib import Path
# import os
# import dj_database_url  # Add this for AWS RDS

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Quick-start development settings - unsuitable for production
# SECRET_KEY = 'django-insecure-$&6d+m+$cum(+6n4voo(7r$3k!^+b11%f3^5ex2cr12a!-xiz#'
# DEBUG = True  # Set to False for production
# ALLOWED_HOSTS = ['to-do-list', 
#                  'localhost', 
#                  '127.0.0.1', 
#                  'https://To-Do-List.com', 
#                  'To-Do-List',
#                  'https://to-do-list-f102be19b0d3.hosted.ghaymah.systems/', 
#                  'to-do-list-f102be19b0d3.hosted.ghaymah.systems/',
#                  'https://to-do-list-f102be19b0d3.hosted.ghaymah.systems', 
#                  'to-do-list-f102be19b0d3.hosted.ghaymah.systems',
#                  ]

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'crud',
#     'corsheaders',  # 
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
# ]

# CORS_ALLOWED_ORIGINS = [
#     "https://to-do-list-f102be19b0d3.hosted.ghaymah.systems",
#     "http://localhost:8000",
#     "https://to-do-list.com",  # If using a custom domain
#     "https://www.to-do-list.com",
# ]

# ROOT_URLCONF = 'ToDoList.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'ToDoList.wsgi.application'  # Uncomment this

# # Default to SQLite for local development
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# # Override with DATABASE_URL if provided (for production)
# if 'DATABASE_URL' in os.environ:
#     DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# APPEND_SLASH = True

# # Add database URL parsing for production
# # DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)