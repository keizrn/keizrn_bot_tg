import requests
import io


from core.settings import settings

ICONS = {
    '01d': '🌞',
    '02d': '🌤',
    '03d': '🌥',
    '04d': '☁️',
    '09d': '🌧',
    '10d': '🌦',
    '11d': '🌩',
    '13d': '❄️',
    '50d': '🌫',
    '01n': '🌙',
    '02n': '🌒',
    '03n': '🌥',
    '04n': '☁️',
    '09n': '🌧',
    '10n': '🌦',
    '11n': '🌩',
    '13n': '❄️',
    '50n': '🌫',
}


def init(user_data):
    search_type = user_data['weather_type']
    if search_type == 'find':
        city = user_data['city']
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'q': city, 'type': 'like', 'units': 'metric', 'lang': 'ru',
                                   'APPID': settings.bots.appid})
        data = res.json()
        if not data['count']:
            return 0
        return generate_result(data, city)
    elif search_type == 'weather':
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                           params={'lat': user_data['lat'], 'lon': user_data['lon'], 'type': 'like', 'units': 'metric',
                                   'lang': 'ru',
                                   'APPID': settings.bots.appid})
        data = res.json()
        return generate_result(data, data['list'][0]['name'])


def generate_result(data, city):
    temp = data['list'][0]['main']['temp']
    feels_like = data['list'][0]['main']['feels_like']
    pressure = (data['list'][0]['main']['pressure']) * 0.75
    humidity = data['list'][0]['main']['humidity']
    wind_speed = data['list'][0]['wind']['speed']
    # rain = 'не ожидается' if data['list'][0]['rain'] is None else 'ожидается'
    # snow = 'не ожидается' if data['list'][0]['snow'] is None else 'ожидается'
    weather = data['list'][0]['weather'][0]['description']
    icon = data['list'][0]['weather'][0]['icon']
    return f'''
    
    
    
<b>Актуальная погода в городе {city}</b>

Температура {round(temp, 1)} °C
Ощущается как {round(feels_like, 1)} °C
Статус: {weather} {ICONS[icon]} 
Давление {round(pressure, 1)} мм рт ст 
Влажность {humidity} %
💨 Скорость ветра {wind_speed} м/с 💨
'''
