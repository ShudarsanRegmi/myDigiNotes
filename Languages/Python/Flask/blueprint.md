# Blueprint in Flask

Here's a comprehensive, snippet-oriented guide to **Flask Blueprints**, covering all essential aspects:

---

# **Flask Blueprints Guide**

### 1. **What is a Blueprint?**
- A **Blueprint** in Flask is a way to organize your application into modular, reusable components.
- It allows you to group routes, templates, static files, and other resources under a logical structure.

---

## My Snippets

### Directory Structure
```
├── admin
│   ├── admin.py
│   ├── __pycache__
│   │   └── admin.cpython-310.pyc
│   └── templates
│       └── home.html
├── app.py
├── __pycache__
│   └── app.cpython-310.pyc
└── views
    ├── __pycache__
    │   └── views.cpython-310.pyc
    └── views.py

6 directories, 7 files
```

### app.py : registering blueprints
```python
from flask import Flask
from views.views import views
from admin.admin import admin

app = Flask(__name__)

app.register_blueprint(views)
app.register_blueprint(admin)


@app.route("/")
@app.route("/home")
def mainpage():
    return "this is the main page"

if __name__ == "__main__":
    app.run(debug=True)
```

### admin.py : Creating admin blueprint
```python
from flask import Blueprint, render_template


admin = Blueprint("admin", __name__, url_prefix='/admin', template_folder="templates")


@admin.route("/")
def adminhome():
    print("hello....")
    return render_template("home.html")
```

### views.py : Creating views blueprint 
```python
from flask import Blueprint


views = Blueprint("views", __name__, url_prefix="/views")


@views.route("/")
def hello():
    return "this is the home page"
```
---

## ChatGPT Guide

### 2. **Creating a Blueprint**

**Example: `auth.py`**
```python
from flask import Blueprint

# Create a Blueprint instance
auth = Blueprint('auth', __name__)

# Define routes under the blueprint
@auth.route('/login')
def login():
    return "This is the login page."

@auth.route('/logout')
def logout():
    return "This is the logout page."
```

---

### 3. **Registering a Blueprint**
You must register a blueprint with the main Flask application.

**Example: `app.py`**
```python
from flask import Flask
from auth import auth  # Import the Blueprint

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
```

**Explanation:**
- `url_prefix='/auth'`: All routes in the `auth` blueprint will be prefixed with `/auth`.  
  - `/login` becomes `/auth/login`
  - `/logout` becomes `/auth/logout`

---

### 4. **Blueprint with Templates**
**Folder Structure:**
```
project/
├── app.py
├── auth/
│   ├── __init__.py
│   ├── templates/
│   │   └── login.html
```

**Blueprint Code (`auth/__init__.py`):**
```python
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/login')
def login():
    return render_template('login.html')
```

**Template (`auth/templates/login.html`):**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Welcome to the Login Page</h1>
</body>
</html>
```

---

### 5. **Blueprint with Static Files**
**Folder Structure:**
```
project/
├── app.py
├── auth/
│   ├── __init__.py
│   ├── static/
│   │   └── style.css
```

**Blueprint Code (`auth/__init__.py`):**
```python
auth = Blueprint('auth', __name__, static_folder='static')

@auth.route('/static_example')
def static_example():
    return "<link rel='stylesheet' href='/auth/static/style.css'>"
```

**Static File (`auth/static/style.css`):**
```css
body {
    background-color: #f0f0f0;
}
```

---

### 6. **Blueprint with Error Handlers**
Blueprints can have custom error handlers.

**Example:**
```python
@auth.errorhandler(404)
def not_found(e):
    return "Auth Page Not Found", 404
```

---

### 7. **Blueprint with Middleware**
You can attach middleware specific to a blueprint.

**Example:**
```python
@auth.before_request
def before_request():
    print("This runs before any request in the auth blueprint.")
```

---

### 8. **Nested Blueprints**
You can organize blueprints hierarchically.

**Example:**
```python
from flask import Blueprint

admin = Blueprint('admin', __name__)
user = Blueprint('user', __name__)

@admin.route('/dashboard')
def admin_dashboard():
    return "Admin Dashboard"

@user.route('/profile')
def user_profile():
    return "User Profile"

# Register both blueprints in the main app
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
```

---

### 9. **Blueprint with Configuration**
Blueprints can use app configuration or have their own.

**Example:**
```python
@auth.route('/config')
def config_demo():
    return f"SECRET_KEY is: {current_app.config['SECRET_KEY']}"
```

**In `app.py`:**
```python
app.config['SECRET_KEY'] = 'your-secret-key'
```

---

### 10. **Combining Multiple Blueprints**
**Example:**
```python
from flask import Flask
from auth import auth
from user import user

app = Flask(__name__)

# Register multiple blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(user, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 11. **Testing a Blueprint**
Use Flask's `test_client()` for unit testing blueprints.

**Example:**
```python
def test_auth(client):
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b"Login" in response.data
```

---

### Summary of Key Points
- **Blueprints are reusable modules** for organizing routes, templates, static files, and error handlers.
- They enable **clean code** and scalability in large applications.
- Register a blueprint with `app.register_blueprint()`.
- Use `url_prefix` to namespace routes.
- Blueprints can have their **own templates, static files, and middleware**.

--- 
