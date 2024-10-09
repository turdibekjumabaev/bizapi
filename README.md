# BizAPI
**A Lightweight Web Framework for Python**

---

## A Simple Example

````python
from bizapi import BizAPI
from bizapi.types import Request, Response

app = BizAPI()


@app.route('/home')
def home(request: Request, response: Response):
    response.text = 'This is the home page'
````
````shell
gunicorn main:app
````

---

## Features (To-Do)
Here's a list of upcoming features that will be included in OneAPI:

 - [X] **Function-Based Routing**
 - [ ] **Parameterized Routing**
 - [ ] **Class-Based Handlers**
 - [ ] **Allowed Methods**
 - [ ] **Django Routes Compatibility**
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