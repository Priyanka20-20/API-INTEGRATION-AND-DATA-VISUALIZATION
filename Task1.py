import requests
import matplotlib.pyplot as plt


# SINGLE CITY DATA

API_Key = '6d445795b16274093b314a5533448977'
City_name = 'Mumbai'

url = f'https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={API_Key}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print('Weather is:', data['weather'][0]['description'])
    print('Current Temperature:', data['main']['temp'])
    print('Feels like:', data['main']['feels_like'])
    print('Humidity:', data['main']['humidity'])

    # Graph for single city
    temp = data['main']['temp']
    humidity = data['main']['humidity']

    labels = ['Temperature', 'Humidity']
    values = [temp, humidity]

    plt.bar(labels, values, color=['red', 'blue'])
    plt.title("Mumbai Weather Data")
    plt.ylabel("Values")
    plt.show()


# MULTIPLE CITIES DATA

cities = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata']
temperatures = []

for city in cities:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric'
    
    response = requests.get(url)
    data = response.json()

    temperatures.append(data['main']['temp'])

# Graph OUTSIDE loop
plt.bar(cities, temperatures, color=['green', 'orange', 'purple', 'blue'])
plt.title("Temperature of Different Cities")
plt.ylabel("Temperature (°C)")
plt.xlabel("Cities")
plt.show()
