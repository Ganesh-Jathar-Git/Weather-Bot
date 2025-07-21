import requests
import os
from dotenv import load_dotenv
load_dotenv() 
# Use of environment variables
API_KEY = os.getenv("WEATHER_API_KEY")
#Function to get the City weather from weather API 
def get_weather(city: str) -> str:
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&lang=ja"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    if response.status_code != 200:
        return "天気情報が取得できませんでした。"

    data = response.json()
    try:
        desc = data["current"]["condition"]["text"]
        temp = data["current"]["temp_c"]
        return f"{city}の現在の天気は{desc}、気温は{temp}度です。"
    except KeyError as e:
        print(f"KeyError: {e}")
        return "天気情報の解析に失敗しました。"
