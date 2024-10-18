<p align="center">
  <a href="https://telegra.ph/BizAPI-10-18"><img src="https://raw.githubusercontent.com/turdibekjumabaev/turdibekjumabaev/refs/heads/main/host/Logo%20BizApi%20Black.png" alt="BizAPI"></a>
</p>

<p align="center">A Lightweight Web Framework for Python</p>

<p align="center">
    <img alt="PyPI - License" src="https://img.shields.io/pypi/l/BizAPI">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/BizAPI">
    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/BizAPI">
</p>
<p align="center">
    <a href="https://github.com/turdibekjumabaev/bizapi" target="_blank"><b>Source Code</b></a> and <a href="https://telegra.ph/BizAPI-10-18" target="_blank"><b>Information</b></a> about BizAPI
</p>

---

## Contents

  * [Installation](#installation)
  * [Quick Start](#quick-start)
  * [Routing](#routing)
    * [Function-Based](#function-based-routing)
    * [Parameterized](#parameterized-routing)
    * [Allowed Methods](#allowed-methods)
    * [Class-Based](#class-based-routing)
    * [Simple Router](#simple-router)
  * [Templates](#templates)
  * [Exception Handler](#exception-handler)
  * [Custom Responses](#custom-response)
  * [Middleware](#middleware)

---

## Installation

To install BizAPI, use the following command:
```
pip install BizAPI
```

---

## Quick Start
Create a simple application using BizAPI:
````python
from bizapi import BizAPI
from bizapi.types import Request, Response

app = BizAPI()


@app.route('/')
def home(request: Request, response: Response):
    response.text = 'This is the home page'

````
Run the application using Gunicorn:
````shell
gunicorn main:app
````

---
## Routing
### Function-Based Routing
```python
@app.route('/')
def index(request: Request, response: Response):
    response.text = "Hello World!"
```

### Parameterized Routing
```python
@app.route('/say-hello/{name}')
def sayhello(request: Request, response: Response, name: str):
    response.text = f"Assalawma áleykum {name}"
```

### Allowed Methods
```python
@app.route('/article', methods=['POST'])
def create_article(request: Request, response: Response):
    # Create a new article
    pass


@app.route('/article', methods=['GET'])
def get_article(request: Request, response: Response):
    # Get an article
    pass
```

You can also use the method-specific decorators:
```python
@app.post('/article')
def create_product(request: Request, response: Response):
    # Create a new article
    pass


@app.get('/article')
def get_product(request: Request, response: Response):
    # Get an article
    pass
```

### Class-Based Routing
```python
@app.route('/article')
class Article:
    def get(request: Request, response: Response):
        # Get an article
        pass
    
    def post(request: Request, response: Response):
        # Create a new article
        pass
```

### Simple Router
```python
def create_article(request: Request, response: Response):
    response.text = "A new article has been created"


app.register_route('/article', create_article, ['POST'])
```

---

## Templates

```python
from bizapi import render_template

@app.route('/hello')
def hello_page(request: Request, response: Response):
    response.html = render_template('hello.html', name="John")



# Second way
@app.route('/say-hello', methods=['GET'])
def home_page(request: Request, response: Response):
    response.html = render_template('hello.html', {
        'title': 'Say Hello!',
        'name': 'John'
    })
```

`templates/hello.txt`
```html
<html>
    <head><title>Hello</title></head>
    <body><p>Hello, {{name}}</p></body>
</html>
```

---

## Exception Handler
Add a custom exception handler to manage errors:
```python
def on_exception(request: Request, response: Response, exc: Exception):
    response.text = str(exc)


app.add_exception_handler(on_exception)
```

---

## Custom Response
BizAPI allows returning different types of responses:
```python
@app.route('/json')
def json(request: Request, response: Response):
    response.json = {'message': 'Hello, World'}
```
```python
@app.route('/text')
def text(request: Request, response: Response):
    response.text = "Hello World"
```
```python
@app.route('/html')
def html(request: Request, response: Response):
    response.html = "<h1>Hello, World</h1>"
```

---

## Middleware
You can add middleware to process requests and responses:
```python
from bizapi.middleware import Middleware

class CustomMiddleware(Middleware):
    def request(self, request: Request):
        print(f"Request received: {request.path}")

    def response(self, request: Request, response: Response):
        print(f"Response sent for: {request.path}")

app.add_middleware(CustomMiddleware)

```

---

**License**  
This project is licensed under the [MIT License](https://opensource.org/license/mit).
