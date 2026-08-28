from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
    "Aarav Sharma": 85,
    "Aditi Verma": 92,
    "Rohan Desai": 78,
    "Sneha Iyer": 88,
    "Kabir Singh": 95,
    "Ananya Patel": 81,
    "Vivan Joshi": 76,
    "Meera Reddy": 89,
    "Aryan Kapoor": 94,
    "Zara Bisht": 72,
    "Dev Malhotra": 83,
    "Riya Das": 90,
    "Yash Gupta": 79,
    "Ishita Rao": 91,
    "Sahil Ahuja": 87
}
    return render_template("index.html", marks=marks)

app.run(debug=True)