from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form['city']
    api_key = "86f233aea620d9494aa0b705086ebbe8"  # Replace with one's specific OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data.get("cod") != 200:
        return f"Error: {data.get('message', 'Something went wrong!')}"
    
    weather = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }
    return render_template('weather.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
