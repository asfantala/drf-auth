# Django_Docker - LAB - Class 33
## Project: Authentication & Production Server
### Author: Tala Asfan

### Installation 

1. Create and activate a virtual environment:
```
 python -m venv venv 
 source venv/bin/activate
```
2. Install the project dependencies:
```
pip install -r requirements.txt

```
### Setup
- you need to have docker installed on your machine
### Features - Docker
- Switch from Django's development server to using Gunicorn.
   - pip install gunicorn 
   - edit the command inside the docker-compose.yml to this :
    > gunicorn myapp.wsgi:application --bind 0.0.0.0:8000 --workers 4
   - To handle static files on the Django side using Whitenoise.
        - add a middleware in sitting.py:     'whitenoise.middleware.WhiteNoiseMiddleware',
        - in settings.py : 
        ```
        STATIC_DIR = os.path.join(BASE_DIR, 'static')
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        STATIC_URL = 'static/'
        STATICFILES_DIRS = [
        STATIC_DIR,
        ]
        ```
        - run command : python manage.py collectstatic

### How to initialize/run your application
- docker compose up


### To manually test the API using an HTTP client such as HTTPie or ThunderClient, follow these steps:

- Get Tokens:

    - URL: /api/token/
    - Method: POST
    - Token: Not required
    - Description: Send a POST request to this endpoint with the appropriate credentials to obtain access and refresh tokens.

- Refresh Tokens:

    - URL: /api/token/refresh/
    - Method: POST
    - Token: Refresh token required
    - Description: Send a POST request to this endpoint with a valid refresh token to obtain a new access token.    
### Tests
- python manage.py test


- http://localhost:8000/api/v1/items/
- http://localhost:8000/api/v1/items/post/
