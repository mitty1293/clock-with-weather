#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import keys

def gen_url():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={key}"
    formatted_url=url.format(key=keys.API_KEY, lat=keys.LAT, lon=keys.LON)
    return formatted_url