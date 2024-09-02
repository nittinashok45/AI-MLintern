from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = '##############   '  
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def get_weather_by_city(city_name):
    url = f"{BASE_URL}weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast_by_city(city_name):
    url = f"{BASE_URL}forecast?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_weather_by_location(lat, lon):
    url = f"{BASE_URL}weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_forecast_by_location(lat, lon):
    url = f"{BASE_URL}forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def get_user_location():
    # Use an IP geolocation API to get user's location based on IP
    response = requests.get('https://ipapi.co/json/')
    data = response.json()
    return data['latitude'], data['longitude']

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather_by_city(city)
            forecast_data = get_forecast_by_city(city)
    else:
        lat, lon = get_user_location()
        weather_data = get_weather_by_location(lat, lon)
        forecast_data = get_forecast_by_location(lat, lon)

    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
