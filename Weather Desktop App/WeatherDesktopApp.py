#an app that presents weather of city you want
#using a GUI

import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=472ad775865e82e6b711fca01ae4a756"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(((json_data['main']['temp'] - 273.15)*1.8+32))
    min_temp = int(((json_data['main']['temp_min'] - 273.15)*1.8+32))
    max_temp = int(((json_data['main']['temp_max'] - 273.15)*1.8+32))
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°F"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°F" + "\n" + "Max Temp: " + str(
        max_temp) + "°F" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()