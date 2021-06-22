import requests

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display the data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_des = api_data['weather'][0]['description']
humdty = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather des  :", weather_des)
print("Current Humidity      :", humdty, '%')
print("Current wind speed    :", wind_speed, 'kmph')

# opening the file
file = open("weather_data.txt", 'a')

# #create variables to store and save the data
heading = "\n\n\t\tWeather Stats for - {}  || {}\n\n".format(location.upper(), date_time)
city_name = "Current temperature is: {:.2f} deg C\n".format(temp_city)
weather_des = "Current weather desc  : {}\n".format(weather_des)
humidity = "Current Humidity      : {}% \n".format(humdty)
wind_speed = "Current wind speed    : {} Kmph \n"

# Writing all data in the file
file.write(
        heading + city_name + weather_des + humidity + wind_speed
    )

# Closing the file
file.close()
