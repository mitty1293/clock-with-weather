import datetime

def of_hourly(**weather_data: dict) :
    for i in range(12):
        item = weather_data['hourly'][i]
        dt = datetime.datetime.fromtimestamp(item['dt'])

def of_daily(**weather_data: dict) :
    pass