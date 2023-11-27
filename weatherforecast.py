from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = '243d0b5c58eeaf940b0a72323689f1ba'
BASE_URL = 'http://127.0.0.1:5000/weather?city=delhi'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({'error': 'City parameter is required'}),400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # You can change the units as per your preference
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
            return jsonify(weather)
        else:
            return jsonify({'error': data['message']}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
