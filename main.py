import requests
import os
import sys
# 2 - реализовать прогноз погоды через API (например https://openweathermap.org/current
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# (ключ Дмитрия Судницына )). Вводится город - отображается текущая погода в этом городе
# key="Тут должен быть ключь"


def reg_wether(city="LONDON", key="", unit="metric"):
    lst = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units={unit}'
    r = requests.get(lst)
    return r.json()

def print_wether(weath_json):
     print(f"Страна {weath_json['sys']['country']} город {weath_json['name']}  ")
     print(f"Географическое положение города, долгота = {weath_json['coord']['lon']}")
     print(f"Географическое положение города, широта = {weath_json['coord']['lat']}")
     main_l = weath_json['main']
     print(f"Темперетура = {main_l['temp']}")
     print(f"Минимальная температура = {main_l['temp_min']}")
     print(f"Максимальная температура = {main_l['temp_max']}")
     print(f"Атмосферное давление hPa =  {main_l['pressure']}")
     print(f"Влажность % =  {main_l['humidity']}")
     input("Нажмите Enter")

while True:
 print("Программа показа погоды по городам")
 print("1 Показать погоду по городу")
 print("2 Выйти из программы")
 n=input("Какой пункт выбираете? ")
 if int(n)==1:
    os.system('cls||clear')
    city=input("Введите город латинскими буквами: ")
    weath = reg_wether(city)
    if weath['cod']==200:
     print_wether(weath)
    else:
     print(f"{weath['cod']} {weath['message']} Такого города {city} нет в базе")        
     input("Нажмите Enter")
     os.system('cls||clear')
 if int(n)==2:
    os.system('cls||clear')
    sys.exit()      

# Macau
# Esbjerg  
# Roskilde
# Alexandria
# Beni Ebeid Таког города нет в базе
# Paris