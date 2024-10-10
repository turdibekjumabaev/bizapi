# <p align="center"> BizAPI </p>
<p align="center">A Lightweight Web Framework for Python</p>

---

## Contents

  * [A Simple Example](#a-simple-example)
  * Routing
    * [Function-Based](#function-based-routing)
    * [Parameterized](#parameterized-routing)
    * [Allowed Methods](#allowed-methods)
    * [Class-Based](#class-based-routing)
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
from bizapi import BizAPI
from bizapi.types import Request, Response

app = BizAPI()


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

---

## Features (To-Do)
Here's a list of upcoming features that will be included in BizAPI:

 - [X] **Function-Based Routing**
 - [X] **Parameterized Routing**
 - [X] **Allowed Methods**
 - [X] **Class-Based Routing**
 - [ ] **Django Routes**
 - [ ] **Exception Handler**
 - [ ] **Templates**
 - [ ] **Static Folder**
 - [ ] **Custom Response**
 - [ ] **Middleware**  

---

**License**  
This project is licensed under the [MIT License](https://opensource.org/license/mit).

---
[**Community of Lazy People**](https://t.me/judaerinshek)