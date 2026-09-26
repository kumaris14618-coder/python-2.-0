import requests  #a weather api
import matplotlib.pyplot as plt
#we need coordinates to get weather data
latitude = 48.85  #paris latitude
longitude = 2.35  #paris longitude


#build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"


#make a request
response = requests.get(url)
data = response.json()

print(data)
#data.keys()

temperature = data["current"]["temperature_2m"]
print(temperature)

