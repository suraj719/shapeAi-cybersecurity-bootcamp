import requests
from datetime import datetime
 
api_key = '69a90bbbeeda65396fcb36cc97703f11'
location = input("Enter the city name: ")
 
comp_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(comp_api_link)
api_data = api_link.json()
 
 
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
file = open("weatherdata.txt","w")
 
file.write("\n")
file.write ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
 
file.write ("\n")
 
file.write("Current temperature is: {:.2f} deg C".format(temp_city))
 
file.write("\n")
 
file.write("Current weather desc  :"+ str(weather_desc))
 
file.write("\n")
 
file.write("Current Humidity      :"+ str(hmdt) + "%")
 
file.write("\n")
 
file.write("Current wind speed    :" + str(wind_spd) + "kmph")
 
file.close ()

print ("\n")
print ("The weather details for "+ location +" have been successfully sent to weatherdata.txt file.")
 
