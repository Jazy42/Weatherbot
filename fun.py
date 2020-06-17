import requests
from bs4 import BeautifulSoup
import sqlite3

from forcecat import Forecast


#
conn = sqlite3.connect('WEATHERR.db')
c = conn.cursor()
# # c.execute("""CREATE TABLE cities(
#             cityid integer  PRIMARY KEY AUTOINCREMENT,
#             nameofcity text,
#             zipcode integer,
#             country text
#             ) """)# c.execute('DROP TABLE forecasts')
# c.execute("""CREATE TABLE forecasts(
#                 id INTEGER PRIMARY KEY,
#                 city_id INTEGER,
#                 day UNICODE,
#                 temperature real,
#                 descs text,
#                 created_at datetime,
#                updated_at datetime
#                 )""")

urls = [ #'https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567',
        'https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977',
        'https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453',
        'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324',
        'https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196',
        'https://forecast.weather.gov/MapClick.php?lat=30.2676&lon=-97.743',
        #'https://forecast.weather.gov/MapClick.php?lat=32.7157&lon=-117.1617', change url
        'https://forecast.weather.gov/MapClick.php?lat=29.7608&lon=-95.3695',
        'https://forecast.weather.gov/MapClick.php?lat=39.74&lon=-104.992',
        'https://forecast.weather.gov/MapClick.php?lat=42.3317&lon=-83.048',
        ]
for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(id='seven-day-forecast-body')
    items = week.find_all(class_='forecast-tombstone')

    days = item.find(class_="period-name").get_text() for item in items:
    descss = item.find(class_="short-desc").get_text() for item in items:

    temperaturee = item.find(class_="temp").get_text() for item in items:
    print(temperaturee)
    print(days)
    print(descss)
    print('----------------------------------------------------------------')
c.execute("INSERT INTO forecasts(day,descs,temperature)VALUES(:day,:descs,:temperature)",{'day' : str(days) , 'temperature' : str(temperaturee) , 'descs':str(descss)})

conn.commit()
conn.close()








#
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_1.name , 'Zipcode':city_1.Zipcode,'country':city_1.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_2.name , 'Zipcode':city_2.Zipcode,'country':city_2.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_3.name , 'Zipcode':city_3.Zipcode,'country':city_3.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_4.name , 'Zipcode':city_4.Zipcode,'country':city_4.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_5.name , 'Zipcode':city_5.Zipcode,'country':city_5.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_6.name , 'Zipcode':city_6.Zipcode,'country':city_6.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_7.name , 'Zipcode':city_7.Zipcode,'country':city_7.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_8.name , 'Zipcode':city_8.Zipcode,'country':city_8.country})
# c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_9.name , 'Zipcode':city_9.Zipcode,'country':city_9.country})

#c.execute("SELECT * FROM CITIES")




# conn.commit()
# conn.close()


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
















































#
# weather_stuff = pd.DataFrame(
#     {
#         'Day': day,
#         'Description': descs,
#         'temp' : tems,
#     })
# print(weather_stuff)
# #weather_stuff.to_csv('weather.csv')\\\


