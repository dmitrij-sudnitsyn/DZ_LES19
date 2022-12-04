import requests
import os
import sys
# 2 - реализовать прогноз погоды через API (например https://openweathermap.org/current
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?q={city}&appid=aee9cfbc9cb6480b6ebe19a887b288cf&units=metric
# (ключ Дмитрия Судницына aee9cfbc9cb6480b6ebe19a887b288cf)). Вводится город - отображается текущая погода в этом городе


def reg_wether(city="LONDON", key="aee9cfbc9cb6480b6ebe19a887b288cf", unit="metric"):
    lst = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={unit}'
    r = requests.get(lst)
    return r.json()

def print_wether(weath_json):
    # if weath_json['cod']=='200':
     print(weath_json)
     print(f"Страна {weath_json['sys']['country']} город {weath_json['name']}  ")
     print(f"Географическое положение города, долгота = {weath_json['coord']['lon']}")
     print(f"Географическое положение города, широта = {weath_json['coord']['lat']}")
     main_l = weath_json['main']
     print(f"Темперетура = {main_l['temp']}")
     print(f"Минимальная температура = {main_l['temp_min']}")
     print(f"Максимальная температура = {main_l['temp_max']}")
     print(f"Атмосферное давление hPa =  {main_l['pressure']}")
     print(f"Влажность % =  {main_l['humidity']}")
     input("Нажмите любую клавишу ")
    # else:
    #  print(f"Такого города нет в базе {weath_json['code']} {weath_json['message']}")    

while True:
 print("Программа показа погоды по городам")
 print("1 Показать погоду по городу")
 print("2 Выйти из программы")
 n=input("Какой пункт выбираете? ")
 if int(n)==1:
    os.system('cls||clear')
    city=input("Введите город латинскими буквами: ")
    weath = reg_wether(city)
    if weath['cod']=='200':
     print_wether(weath)
    else:
     print(f"Такого города нет в базе {weath['cod']} {weath['message']}")        
     os.system('cls||clear')
 if int(n)==2:
    os.system('cls||clear')
    sys.exit()      

# Macau
# Esbjerg  
# Roskilde
# Alexandria
# Beni Ebeid