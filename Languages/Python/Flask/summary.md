# Flask Summary


## Directory Structure
```python
my-flask-app
   ├── static/
   │   └── css/
   │       └── main.css
   ├── templates/
   │   ├── index.html
   │   └── student.html
   ├── data.py
   └── students.py
```

## Important imports
```python
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from flask import render_template
```

## Creating a basic flask application

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, I'm a flask app"


if __name__ == "__main__":
    app.run(debug=True)
```

## Handling Post Requests
```python
@app.route('/post', methods=['POST'])
def post_example():
    data = request.get_json()
    return jsonify({"received_data": data}), 201
```

## Handling Path Parameters
```python
@app.route("/path/<params>")
def pathparams(params):
    res = "<b> This route is for demonstrating path parameters in flask </b>"
    res += "<br> The value of params is: " + params
    return res
```
## Making a custom response
```python
@app.route('/custom_response')
def custom():
    response = make_response("Custom Response", 200)
    response.headers["Conent-Type"] = "text/plain"
    return response
```

## Responding With Json
```python
@app.route("/json")
def json():
    return jsonify({"key1": "value1", "key2": "value2"})
```

## Checking different request attributes
```python
@app.route("/request_handling", methods=['GET', 'POST'])
def request_handling():
    res = ""
    res += f"Request Method = {request.method} <br>"
    res += f"Query params = {request.args} <br>"
    res += f"Request Form = {request.form} <br>"
    # res += f"Json Data = {request.get_json()} <br>"
    res += f"Request Data = {request.data} <br>"
    res += "<br> <b> Headers </b> <br>"
    for header, value in request.headers.items():
        res += f"{header}: {value} <br>"
    return res
```

## Responding with a template
```python
@app.route("/template/") # handling the case of no path params
@app.route("/template/<name>")
def template(name=None):
    return render_template('homepage.html', name=name or "User")
```

## Other Important Topics To Cover
- ORM SQL Alchemy
- Flask Login for Session Management
- Flask form for Dealing With forms
- Working With Clould flare app



