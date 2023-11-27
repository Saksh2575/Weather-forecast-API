# Weather-forecast-API
# Single-Parameter Weather Forecast API

## Overview

This API provides a simple way to obtain weather forecast data for a specific city. Built with Python and Flask, it fetches accurate weather information from OpenWeatherMap.

## Features

- **City-based Forecast:** Retrieve weather forecasts by providing the name of the city.
- **Simplicity:** Easy to use with a single query parameter.
- **Error Handling:** Gracefully handles errors for a smooth user experience.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- An API key from OpenWeatherMap. Obtain one [here](https://openweathermap.org/api).

### Installation

1. **Install dependencies:**

    ```bash
    pip install Flask requests
    ```

2. **Replace API_KEY placeholder:**

    - Open `app.py` in a text editor.
    - Replace `'YOUR_API_KEY'` with your actual OpenWeatherMap API key.

### Usage

1. **Start the API:**

    ```bash
    python app.py
    ```

   This will start the Flask development server.

2. **Make a GET request:**

    Use your preferred tool (e.g., Postman, cURL) to make a GET request to:

    ```http
    GET /weather?city=CityName
    ```

    Replace `CityName` with the desired city parameter.

3. **Receive weather forecast data in the response.**

## API Endpoint

- **GET /weather**

   Parameters:
   - `city`: City name (required)

   Example:
   ```http
   GET /weather?city=London
SCREENSHOTS:

![Screenshot (42)](https://github.com/Saksh2575/Weather-forecast-API/assets/137802909/80649103-1f29-4b3e-b1d0-c6889ac79510)

![Screenshot (45)](https://github.com/Saksh2575/Weather-forecast-API/assets/137802909/41d9435e-d270-4787-9983-d7b8edda1ee6)



   

