import requests
import os
from dotenv import load_dotenv
load_dotenv()
weather_api_key = os.environ["WEATHER_API_KEY"]
while(True):
    try:
        user_prompt = input("Enter a zip code or city to get the tempature of: ")
        result = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&aqi=no&q={user_prompt}")
        json_result = result.json()
        location = json_result["location"]["name"]
        temp = json_result["current"]["temp_f"]
        print(f"The tempature in {location} is {temp} degrees farnheit")
        break
    except:
        print("Invalid zip code or city name try again")
        continue

