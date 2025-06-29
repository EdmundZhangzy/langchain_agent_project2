import requests
from langchain.tools import Tool

def get_weather(city):
    response = requests.get(f"https://wttr.in/{city}?format=3")
    return response.text

weather_tool = Tool(
    name="WeatherTool",
    func=get_weather,
    description="查询某个城市的当前天气。例如：'东京天气如何？'"
)