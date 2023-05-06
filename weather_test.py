import paho.mqtt.client as mqtt
import requests

URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "7c6d9f16cc55e9b5efc85c65a4664696"
	
def get_weather(city: str) -> tuple:

	res = requests.get(URL, params={"q": city, "appid": API_KEY})
	if res.status_code == 200:
		data = res.json()
		if "main" in data:
			humidity = data["main"]["humidity"]
			condition = data["weather"][0]["description"].capitalize()
			temp = data["main"]["temp"]
			return humidity, condition, temp
			
def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code "+str(rc))
    client.subscribe("weather_data")
    
def main():
	cities = ["London", "New York", "Paris", "Tokyo", "Florence", "Los Angeles", "Guangzhou", "Shanghai", "Singapore", "Jakarta", "Hanoi", "Montreal", "Vancouver", "Chicago", "Baku", "Monza", "Perth", "Sydney", "Imola", "Mexico City", "Barcelona", "Lisbon", "Istanbul", "Helsinki", "Copenhagen", "Wellington", "Zurich", "Rome", "Hong Kong", "Dubai", "Madrid", "Seoul", "Spielberg", "Sepang", "Beijing","Cairo", "Cape Town", "Santiago", "Amsterdam", "Athens", "Warsaw", "Mumbai","Osaka", "Buenos Aires", "San Francisco", "Bangkok", "Reykjavik", "Nairobi", "Vienna", "Melbourne", "Houston", "Seattle", "Cleveland", "San Diego", "Denver", "Boston", "Miami", "Orlando", "Salt Lake City", "Provo", "Manila", "Monte Carlo", "Pretoria", "Johannesburg", "Dublin", "Manchester", "Liverpool", "Birmingham", "Leeds", "Brussels", "Frankfurt", "Marseille", "Montpellier", "Turin", "Oslo", "Valencia", "Bilbao", "Vigo", "Nantes", "Kobe", "Hiroshima", "Kyoto", "Nagoya", "Sapporo", "Vladivostok", "Busan", "Ulsan", "Incheon", "Daejeon", "Yantai", "Shenyang", "Qingdao"]
	
	client = mqtt.Client()
	client.on_connect = on_connect
	client.connect("172.20.10.9", 1883, 60) 
	client.loop_start()
	
	for city in cities:
		result = get_weather(city)
		humidity, condition, temp = result
		if "Clear" in condition or "Scatter" in condition or "Few" in condition:
			condition = "1"
		else:
			condition = "2"
		message = f"{humidity}, {temp}, {condition}"
		print(message)
		client.publish("weather_data", message)

	client.loop_stop()
	client.disconnect()

            
if __name__ == "__main__":
	main()
