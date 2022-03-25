import requests

api_keys = 'f2894123f53cc162e5772bc4a05eeb08'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_keys}")

#print(weather_data.status_code)
#print(weather_data.json())

if weather_data.json()['cod'] == "404":
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    #print(weather, temp)
    print(f"The weather in {user_input} is {weather}")
    print(f"The temparature in {user_input} is {temp}°F")