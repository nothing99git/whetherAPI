from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "demo")

@app.route("/")
def home():
    return "✅ Weather API is online."

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City name required"}), 400
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
