import datetime

def of_hourly(**weather_data: dict) :
    for i in range(12):
        after_i_hour = weather_data['hourly'][i]
        dt = datetime.datetime.fromtimestamp(after_i_hour['dt'])
        temp = after_i_hour['temp']
        icon = after_i_hour['weather'][0]['icon']
        description = after_i_hour['weather'][0]['description']
        

def of_daily(**weather_data: dict) :
    pass