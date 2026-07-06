# Python-Flask

🐍 Learning Flask from scratch — routing, templates, forms, and static files. One concept at a time.

---

## What's Inside

### 1. `flask_basics/`
My very first Flask app. One route, one rendered HTML template — just getting a feel for how Flask works.

```
flask_basics/
├── main.py
└── templates/
    └── index.html
```

**Run it:**
```bash
cd flask_basics
pip install flask
python main.py
```
Open `http://127.0.0.1:5000/` in your browser.

---

### 2. `flask_static_site/`
A multi-page Flask site with four routes — Home, About, Services, and Contact — each rendering its own Jinja template. Built to understand how Flask handles multiple pages and URL routing.

```
flask_static_site/
├── main.py
└── templates/
    ├── home.html
    ├── about.html
    ├── services.html
    └── contact.html
```

**Run it:**
```bash
cd flask_static_site
pip install flask
python main.py
```
Open `http://127.0.0.1:5000/` in your browser.

---

### 3. `flask_forms/`
Learning how to handle HTML forms in Flask. The route handles both GET (show form) and POST (receive form data) requests, and saves the submitted name and email to a text file.

```
flask_forms/
├── main.py
└── templates/
    └── contact.html
```

**Run it:**
```bash
cd flask_forms
pip install flask
python main.py
```
Open `http://127.0.0.1:5000/` in your browser.

---

### 4. `serving_static_file/`
Learning how to serve static files in Flask. A simple page with a download link that serves a PDF file from Flask's `static/` folder.

```
serving_static_file/
├── main.py
├── static/
│   └── 1.pdf
└── templates/
    └── index.html
```

**Run it:**
```bash
cd serving_static_file
pip install flask
python main.py
```
Open `http://127.0.0.1:8000/` in your browser.

---

## Tech Stack
- Python
- Flask
- Jinja2

---

## About
This repo is part of my learning journey into backend web development with Flask. Still exploring — more coming as I go deeper.

---

## Author
**Deepanshu Bisht**  
GitHub: [@deepanshu-bisht-dev](https://github.com/deepanshu-bisht-dev)
