import datetime

def of_hourly(**weather_data: dict) -> list:
    hourly_data: list = []
    for i in range(12):
        after_i_hour: dict = weather_data['hourly'][i]
        data: dict = {
            'dt': datetime.datetime.fromtimestamp(after_i_hour['dt']),
            'temp': after_i_hour['temp'],
            'icon': after_i_hour['weather'][0]['icon'],
            'description': after_i_hour['weather'][0]['description'],
            'rain': after_i_hour.get('rain', {'1h': 0}).get('1h')
        }
        hourly_data.append(data)
    return hourly_data

def of_daily(**weather_data: dict) -> list:
    daily_data: list = []
    for i in range()