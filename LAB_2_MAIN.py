import requests
s_city ="Moscow,RU"
appid ="c0dfa5e8162869bf658580cda4daa1f8"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",params={'q': s_city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print(data['main'])
print("Город:", s_city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Ощущается как:", data['main']['feels_like'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Давление:", data['main']['pressure'])
print('Слила ветра сегодня:', )
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'],"> \r\nТемпература<",
        '{0:+3.0f}'.format(i['main']['temp']),"> \r\nПогодныеусловия <",
        i['weather'][0]['description'], "> \r\nСила ветра на сегодня <",
        i['wind']['speed'], 'м/с', '> \r\nВидимость на сегодня <',
        i['visibility'] / 10000 * 100, '%', ">")
    print("____________________________")