
# Project Documentation

## Overview

This project connects a **React** frontend with a **Django** backend. The Django backend provides an API endpoint that the React app fetches data from and displays.

## Running the Project

1. **Start the Django server**:

   ```bash
   python3 manage.py runserver
   ```

2. **Start the React app**:

   ```bash
   npm start
   ```

Visit `http://localhost:3000` to see the message from the Django API.

---

This setup allows the React app to fetch and display data from the Django backend, and both parts of the application can communicate smoothly through CORS configuration.



## Actions Taken

### Django Backend

1. **Created a view**:
    - Added a view in `views.py` to return JSON data (a simple "Hello, World!" message).

   ```python
   def hello_world(request):
       data = {'message': 'Hello, World!'}
       return JsonResponse(data)
   ```

2. **Configured URL routing**:
    - Set up a URL route in `urls.py` to expose the `hello_world` view via the `/api/hello/` endpoint.

   ```python
   urlpatterns = [
       path('api/hello/', views.hello_world, name='hello_world'),
   ]
   ```

3. **Applied migrations** (if needed):
    - Ran `python3 manage.py migrate` to apply any unapplied migrations.

4. **Started the Django server**:
    - Used `python3 manage.py runserver` to run the server at `http://127.0.0.1:8000/`.

---

### React Frontend

1. **Fetched data from Django API**:
    - Set up an API request in `App.jsx` to fetch data from the Django backend (`http://127.0.0.1:8000/api/hello/`).

   ```javascript
   useEffect(() => {
     axios.get('http://127.0.0.1:8000/api/hello/')
       .then(response => setMessage(response.data.message))
       .catch(error => console.error('Error:', error));
   }, []);
   ```

2. **Displayed data**:
    - Displayed the fetched message (`Hello, World!`) on the React app's homepage.

---

### CORS Setup

1. **Installed CORS headers in Django**:
    - Used `django-cors-headers` to handle cross-origin requests, allowing the React frontend (running on port 3000) to communicate with the Django backend (running on port 8000).

2. **Configured CORS middleware** in Django:
    - Added `'corsheaders.middleware.CorsMiddleware'` to `MIDDLEWARE` in `settings.py`.
    - Enabled `CORS_ALLOW_ALL_ORIGINS = True` for development.

---

