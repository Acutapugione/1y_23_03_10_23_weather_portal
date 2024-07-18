# -*- coding: utf-8 -*-

from requests import get
from datetime import datetime


class WeatherApiETL:
    base_url: str = "http://api.openweathermap.org/data/2.5/"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def __get_params(self, location, units: str = "metric"):
        return {
            "q": location,
            "appid": self.api_key,
            "units": units,
        }

    def extract(self, location: str, forecast_type: str) -> dict:
        response = get(
            url=f"{self.base_url}{forecast_type}",
            params=self.__get_params(location=location),
        )
        return response.json()

    def transform(self, data: dict, forecast_type: str) -> dict | list | None:
        if forecast_type == "weather":
            return {
                "humidity": data.get("main", {}).get("humidity"),
                "temp": data.get("main", {}).get("temp"),
                "pressure": data.get("main", {}).get("pressure"),
                "clouds": data.get("clouds", {}).get("all"),
            }
        elif forecast_type == "forecast":
            repaired_data = []
            for item in data.get("list", []):
                date = item.get("dt")
                temp = item.get("main").get("temp")
                repaired_date = datetime.fromtimestamp(date).strftime("%d.%m.%y")
                repaired_data.append(
                    {
                        "date": repaired_date,
                        "temp": temp,
                    }
                )
            return repaired_data
        """
        forecast_type == weather (https://openweathermap.org/current)
        forecast_type == forecast (https://openweathermap.org/forecast5) 
        {
        "base": "stations",
        "clouds": {
            "all": 54
        },
        "cod": 200,
        "coord": {
            "lat": 48.468,
            "lon": 35.0418
        },
        "dt": 1720713795,
        "id": 709930,
        "main": {
            "feels_like": 33.84,
            "grnd_level": 1003,
            "humidity": 21,
            "pressure": 1013,
            "sea_level": 1013,
            "temp": 35.58,
            "temp_max": 35.58,
            "temp_min": 35.58
        },
        "name": "Dnipro",
        "sys": {
            "country": "UA",
            "sunrise": 1720662607,
            "sunset": 1720719611
        },
        "timezone": 10800,
        "visibility": 10000,
        "weather": [
            {
            "description": "рвані хмари",
            "icon": "04d",
            "id": 803,
            "main": "Clouds"
            }
        ],
        "wind": {
            "deg": 42,
            "gust": 7.76,
            "speed": 5.91
        }
        }
        """
        """FOR CURRENT
        Extr: clouds -> all | Transfrorm: 'хмари' -> 54
        main -> humidity, pressure, temp | 
        "Вологість: {humidity}\n
        Тиск: {pressure}\n
        Температура: {temp}"
        """
        """FOR FORECAST5
        list -> [index] -> dt -> | to date(example 12.07.2024){date}
                        -> main -> temp | "Температура {temp}"
        """
        ...

    # def load(self):
    #     ...
