import datetime

def of_hourly(**weather_data: dict) -> list:
    hourly_data: list = []
    for i in range(12):
        hourly_property: dict = weather_data['hourly'][i]
        data: dict = {
            'dt': datetime.datetime.fromtimestamp(hourly_property['dt']),
            'temp': hourly_property['temp'],
            'icon': hourly_property['weather'][0]['icon'],
            'description': hourly_property['weather'][0]['description'],
            'rain': hourly_property.get('rain', {'1h': 0}).get('1h')
        }
        hourly_data.append(data)
    return hourly_data

def of_daily(**weather_data: dict) -> list:
    daily_data: list = []
    for daily_property in weather_data['daily']:
        data: dict = {
            'dt': datetime.datetime.fromtimestamp(daily_property['dt']),
            'temp_max': daily_property['temp']['max'],
            'temp_min': daily_property['temp']['min'],
            'icon': daily_property['weather'][0]['icon'],
            'description': daily_property['weather'][0]['description'],
            'rain': daily_property.get('rain', 0)
        }
        daily_data.append(data)
    return daily_data