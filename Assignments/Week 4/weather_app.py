''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

import requests
import json
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

# OpenWeatherMap API endpoint and API key
url = "http://api.openweathermap.org/data/2.5/weather"
api_key = "c0887ee8e5cdccfcb7c614caf7323c83"


def get_weather(city):
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(url, params=params)
    weather_data = json.loads(response.text)
    return weather_data


def show_weather(city):
    
    weather_data = get_weather(city)
    print(weather_data)
   
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%d/%m/%Y")

    temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
    humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
    sunrise_label.config(text=f"Sunrise: {datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime('%H:%M:%S')}")
    sunset_label.config(text=f"Sunset: {datetime.fromtimestamp(weather_data['sys']['sunset']).strftime('%H:%M:%S')}")
    time_label.config(text=f"Time: {current_time}")
    date_label.config(text=f"Date: {current_date}")

    icon_url = f"http://openweathermap.org/img/w/{weather_data['weather'][0]['icon']}.png"
    icon_response = requests.get(icon_url, stream=True)
    icon_image = Image.open(icon_response.raw)
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo

window = tk.Tk()
window.title("Weather App")
window.geometry("600x400")


city_label = tk.Label(window, text="Enter City:")
city_label.pack(pady=10)

city_entry = tk.Entry(window)
city_entry.pack()

temperature_label = tk.Label(window)
temperature_label.pack()

humidity_label = tk.Label(window)
humidity_label.pack()

wind_speed_label = tk.Label(window)
wind_speed_label.pack()

sunrise_label = tk.Label(window)
sunrise_label.pack()

sunset_label = tk.Label(window)
sunset_label.pack()

time_label = tk.Label(window)
time_label.pack()

date_label = tk.Label(window)
date_label.pack()

icon_label = tk.Label(window)
icon_label.pack()

get_weather_button = tk.Button(window, text="Get Weather", command=lambda: show_weather(city_entry.get()))
get_weather_button.pack(pady=10)


window.mainloop()
