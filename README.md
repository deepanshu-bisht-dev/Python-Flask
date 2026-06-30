# Python-Flask

A collection of beginner-to-intermediate Flask projects built while learning the Flask web framework — covering routing, templates, and multi-page site structure.

## Projects

### 1. flask_basics
A minimal Flask app demonstrating a single route rendering an HTML template.
- `main.py` — Flask app with one route (`/`)
- `templates/index.html` — rendered homepage

**Run it:**
```bash
cd flask_basics
pip install flask
python main.py
```
Visit `http://127.0.0.1:5000/` in your browser.

### 2. flask_static_site
A multi-page Flask site with separate routes for Home, About, Services, and Contact pages, each rendered via Jinja templates. Includes Bootstrap for styling.
- `main.py` — Flask app with four routes (`/`, `/about`, `/services`, `/contact`)
- `templates/` — HTML templates for each page

**Run it:**
```bash
cd flask_static_site
pip install flask
python main.py
```
Visit `http://127.0.0.1:5000/` in your browser.

## Tech Stack
- Python
- Flask
- Jinja2 (HTML templating)
- Bootstrap

## About
This repo is part of my journey learning backend web development with Flask. More routes, features, and projects will be added as I progress.

## Author
**Deepanshu Bisht**
GitHub: [@deepanshu-bisht-dev](https://github.com/deepanshu-bisht-dev)
