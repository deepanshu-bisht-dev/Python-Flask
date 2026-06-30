from flask import Flask, render_template

# Create the Flask application instance
app = Flask(__name__)

# Define a simple route
@app.route("/")
def hello_world():
    return render_template("index.html")

app.run(debug = True)


