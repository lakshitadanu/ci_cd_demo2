#app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"  # This is what gets shown on your website root URL

if _name_ == "__main__":
    app.run(debug=True)