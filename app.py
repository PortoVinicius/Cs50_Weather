import os
import requests

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, redirect, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")

@app.route("/")
def index():
    """Show portfolio of stocks"""
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    
    if request.method == "POST":
        if not request.form.get("username"):
            flash("Must provide username", 403)
            return render_template("login.html")

        elif not request.form.get("password"):
            flash("Must provide password", 403)
            return render_template("login.html")

    try:
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        ) 
        
        if len(rows) != 1 or check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):

            session["username"] = rows[0]["id"]
        
        return redirect("/")
    except:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            flash("Username is required!")
            return render_template("register.html")
        elif not password:
            flash("Password is required!")
            return render_template("register.html")
        elif not confirmation:
            flash("Password confirmation is required!")
            return render_template("register.html")

        if password != confirmation:
            flash("Passwords do not match!")
            return render_template("register.html")

        hash = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            return redirect("/")
        except:
            flash("Username has already been registered!")
            return render_template("register.html")

    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/weather", methods=["GET", "POST"])
def get_weather():

    if request.method == "POST":     

        city = request.form.get("city").title()
        request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
        weather_data = requests.get(request_url).json()   
        
        try:
            return render_template("weather.html",                
                name = city,
                humidity = f"{weather_data['main']['humidity']}",
                feels_like = f"{weather_data['main']['feels_like']:.1f}",
                temp_max = f"{weather_data['main']['temp_max']:.1f}",
                temp_min = f"{weather_data['main']['temp_min']:.1f}",
                speed = f"{weather_data['wind']['speed']:.1f}"
            ) 
        except:
            
            city = "Brumado"
            request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
            weather_data = requests.get(request_url).json()

            flash("Sorry, try again!")
            return render_template("weather.html",
                name = city,
                humidity = f"{weather_data['main']['humidity']}",
                feels_like = f"{weather_data['main']['feels_like']:.1f}",
                temp_max = f"{weather_data['main']['temp_max']:.1f}",
                temp_min = f"{weather_data['main']['temp_min']:.1f}",
                speed = f"{weather_data['wind']['speed']:.1f}"
            )
            
    else:

        city = "Brumado"
        request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
        weather_data = requests.get(request_url).json()

        return render_template("weather.html",
            name = city,
            humidity = f"{weather_data['main']['humidity']}",
            feels_like = f"{weather_data['main']['feels_like']:.1f}",
            temp_max = f"{weather_data['main']['temp_max']:.1f}",
            temp_min = f"{weather_data['main']['temp_min']:.1f}",
            speed = f"{weather_data['wind']['speed']:.1f}"
        )

@app.route("/position", methods=["GET", "POST"])
def position_information():

    if request.method == "POST":
        city = request.form.get("city").title()
        request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'
        weather_data = requests.get(request_url).json()

        try:
            return render_template("position.html",
                city = city, 
                lon = f"{weather_data['coord']['lon']}",
                lat = f"{weather_data['coord']['lat']}"
            )

            return render_template("position.html", lon=lon, lat=lat)

        except:
            flash("Sorry, try again!")
            return render_template("position.html")

    else:
        return render_template("position.html")

if __name__ == "__main__":
    app.run(debug=True)