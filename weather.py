import paho.mqtt.client as mqtt
import csv

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code "+str(rc))
    client.subscribe("weather_data")

def on_message(client, userdata, msg):
    # Parse the message and extract the relevant data
    message = msg.payload.decode('utf-8')
    humidity, pressure, clearness = message.split(',')


    # Write the data to a CSV file
    with open('weather.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([humidity, pressure, clearness])

client = mqtt.Client()
client.on_connect = on_connect
header = ["humidity", "temperature", "clearness"]
with open('weather.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
client.on_message = on_message
client.connect("172.20.10.9", 1883, 60)
client.subscribe("weather_data")
client.loop_forever()
