import datetime as dt
from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv
import os

# idk what this does but it will work
app = Flask(__name__)

# @app.route() essentially creates another page and the function just handles whats on the page
@app.route("/")
def index():
    # Returns the html code on the index.html file
    print("route called successfully!")
    return render_template("index.html")

Base_URL = "https://api.openweathermap.org/data/2.5/weather?"

# runs the app
if __name__ == "__main__":
    app.run(debug=True)