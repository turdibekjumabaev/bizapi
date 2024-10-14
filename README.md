# <p align="center"> BizAPI </p>
<p align="center">A Lightweight Web Framework for Python</p>

<p align="center">
    <img alt="PyPI - License" src="https://img.shields.io/pypi/l/BizAPI">
    <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/BizAPI">
    <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/BizAPI">
</p>

---

## Contents

  * [A Simple Example](#a-simple-example)
  * Routing
    * [Function-Based](#function-based-routing)
    * [Parameterized](#parameterized-routing)
    * [Allowed Methods](#allowed-methods)
    * [Class-Based](#class-based-routing)
    * [Simple Router](#simple-router)
  * [Templates](#templates)
  * [Exception Handler](#exception-handler)
  * [Features](#features-to-do)

---

## A Simple Example

Installation using a Python package manager:
```
pip install BizAPI
```

````python
from bizapi import BizAPI
from bizapi.types import Request, Response

app = BizAPI()


@app.route('/')
def home(request: Request, response: Response):
    response.text = 'This is the home page'

````
````shell
gunicorn main:app
````

---

## Function-Based Routing
```python
@app.route('/')
def index(request: Request, response: Response):
    response.text = "Hello World!"
```

## Parameterized Routing
```python
@app.route('/say-hello/{name}')
def sayhello(request: Request, response: Response, name: str):
    response.text = f"Assalawma áleykum {name}"
```

## Allowed Methods
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

## Class-Based Routing
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

## Simple Router
```python
def create_article(request: Request, response: Response):
    response.text = "A new article has been created"


app.register_route('/article', create_article, ['POST'])
```

---

## Templates

```python
from bizapi import render_template


# First way
@app.route('/say-hello', methods=['GET'])
def home_page(request: Request, response: Response):
    response.html = render_template('hello.html', title="Say Hello!", name="John")


# Second way
@app.route('/say-hello', methods=['GET'])
def home_page(request: Request, response: Response):
    response.html = render_template('hello.html', {
        'title': 'Say Hello!',
        'name': 'John'
    })
```
```html
<!-- File: templates/hello.html -->
<html>
    <head>
        <title>{{title}}</title>
    </head>
    <body>
        <p>Hello {{name}}</p>
    </body>
</html>
```

---

## Exception Handler
```python
def on_exception(request: Request, response: Response, exc: Exception):
    response.text = str(exc)


app.add_exception_handler(on_exception)
```

---

## Custom Response
```python
@app.route('/json')
def json(request: Request, response: Response):
    response_data = {
        'message': 'Hello World',
    }
    response.json = response_data
```
```python
@app.route('/text')
def text(request: Request, response: Response):
    response.text = "Hello World"
```
```python
from bizapi import render_template

@app.route('/html')
def html(request: Request, response: Response):
    response.html = render_template('index.html', text='Say Hello')
```

---

## Features (To-Do)
Here's a list of upcoming features that will be included in BizAPI:

 - [X] **Function-Based Routing**
 - [X] **Parameterized Routing**
 - [X] **Allowed Methods**
 - [X] **Class-Based Routing**
 - [X] **Simple Routes**
 - [X] **Templates**
 - [X] **Static Folder**
 - [X] **Exception Handler**
 - [X] **Custom Response**
 - [ ] **Middleware**  

---

**License**  
This project is licensed under the [MIT License](https://opensource.org/license/mit).
