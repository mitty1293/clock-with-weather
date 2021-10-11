from datetime import datetime, timezone, timedelta
from decimal import Decimal, ROUND_HALF_UP

def convert_unixtime_into_jst(unixtime) -> datetime:
    return datetime.fromtimestamp(unixtime, timezone(timedelta(hours=9)))

def get_icon_url(icon_id: str) -> str:
    url: str = "http://openweathermap.org/img/wn/{icon_id}@2x.png"
    icon_url: str = url.format(icon_id=icon_id)
    return icon_url

def round_to_int(f: float) -> Decimal:
    return Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

def of_hourly(**weather_data: dict) -> list:
    hourly_data: list = []
    for i in range(12):
        hourly_property: dict = weather_data['hourly'][i]
        data: dict = {
            'dt': convert_unixtime_into_jst(hourly_property['dt']).strftime('%H:%M'),
            'temp': round_to_int(hourly_property['temp']),
            'icon': get_icon_url(hourly_property['weather'][0]['icon']),
            'description': hourly_property['weather'][0]['description'],
            'rain': hourly_property.get('rain', {'1h': 0}).get('1h'),
            'pop': hourly_property['pop']
        }
        hourly_data.append(data)
    return hourly_data

def of_daily(**weather_data: dict) -> list:
    daily_data: list = []
    for daily_property in weather_data['daily']:
        data: dict = {
            'dt': convert_unixtime_into_jst(daily_property['dt']).strftime('%m/%d %a'),
            'temp_max': round_to_int(daily_property['temp']['max']),
            'temp_min': round_to_int(daily_property['temp']['min']),
            'icon': get_icon_url(daily_property['weather'][0]['icon']),
            'description': daily_property['weather'][0]['description'],
            'rain': daily_property.get('rain', 0),
            'pop': daily_property['pop']
        }
        daily_data.append(data)
    return daily_data