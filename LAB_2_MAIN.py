import requests
city = "Moscow,RU"
appid = "c0dfa5e8162869bf658580cda4daa1f8"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={"q": city, "units": "metric", "lang": "ru", "APPID": appid})
data = res.json()
print(data)
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Ощущается как:", data['main']['feels_like'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Давление:", data['main']['pressure'])
print('Слила ветра сегодня:', )
print("Прогноз погоды на неделю:")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={"q": city, "units": "metric", "lang": "ru", "APPID": appid})
data = res.json()
print(f"\nПрогноз погоды на неделю:")
for i in data["list"]:
    print(f"={i ['dt_txt']}")
    print(f"Температура              {i['main']['temp']:+.0f}")
    print(f"Минимальная температура  {i['main']['temp_min']}")
    print(f"Максимальная температура {i['main']['temp_max']}")
    print(f"Ощущается как            {i['main']['feels_like']}")
    print(f"Погодные условия         {i['weather'][0]['description']}")
    print("____________________________")
print("Прогноз ветра и видимости на неделю:")
for i in data["list"]:
    print("Дата: ", i['dt_txt'])
    print("Скорость ветра: ", i['wind']['speed'], ' м/с')
    print("Видимость:      ", round((i['visibility'] / 10000) * 100), '%')
    print("____________________________")