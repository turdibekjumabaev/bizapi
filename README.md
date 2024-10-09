# BizAPI
**A Lightweight Web Framework for Python**

---

## Contents

  * [A Simple Example](#a-simple-example)
  * Routing
    * [Function-Based](#function-based-routing)
    * [Parameterized](#parameterized-routing)

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

    
@app.route('/say-hello/{name}')
def sayhello(request: Request, response: Response, name: str):
    response.text = f"Assalawma áleykum {name}"
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
@app.route('/article', methods=['POST'])
def create_article(request: Request, response: Response):
    pass


@app.route('/article', methods=['GET'])
def get_article(request: Request, response: Response):
    pass
```
```python
@app.post('/product')
def create_product(request: Request, response: Response):
    pass


@app.get('/product')
def get_product(request: Request, response: Response):
    pass
```

---

## Features (To-Do)
Here's a list of upcoming features that will be included in BizAPI:

 - [X] **Function-Based Routing**
 - [X] **Parameterized Routing**
 - [X] **Allowed Methods**
 - [ ] **Class-Based Routing**
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