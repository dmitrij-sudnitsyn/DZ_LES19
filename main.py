import requests
# 2 - реализовать прогноз погоды через API (например https://openweathermap.org/current
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aee9cfbc9cb6480b6ebe19a887b288cf&units=metric
# (ключ Дмитрия Судницына aee9cfbc9cb6480b6ebe19a887b288cf)). Вводится город - отображается текущая погода в этом городе


def reg_wether(city="London", key="aee9cfbc9cb6480b6ebe19a887b288cf", unit="metric"):
    lst = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={unit}'
    r = requests.get(lst)
    
    return r.json()
# def print_weather(lst_json):
#     lst_json

city="London"
weath_json = reg_wether()
main_l = weath_json['main']
print(f"Город {city}")
print(f"Темперетура = {main_l['temp']}")
print(f"Минимальная температура = {main_l['temp_min']}")
print(f"Максимальная температура = {main_l['temp_max']}")
print(f"Атмосферное давление hPa =  {main_l['pressure']}")
print(f"Влажность % =  {main_l['Humidity']}")

# print(weath_json)
# for item in weath_json.keys():
#     print(item)
# погода


# for item in main_l:
#    print(f"{item} = {main_l[item]}")

# {'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 
# 'main': {'temp': 5.14, 'feels_like': 1.45, 'temp_min': 4.36, 'temp_max': 5.86, 'pressure': 1016, 'humidity': 81}, 'visibility': 10000, 'wind': {'speed': 5.14, 'deg': 60}, 'clouds': {'all': 100}, 'dt': 1670171653, 'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1670140072, 'sunset': 1670169228}, 'timezone': 0, 'id':
#  2643743, 'name': 'London', 'cod': 200}
