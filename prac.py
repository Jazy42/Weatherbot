import requests
from bs4 import BeautifulSoup
import sqlite3
from cities import City
from datetime import datetime
from datetime import timedelta

conn = sqlite3.connect('test2.db')
c = conn.cursor()

#
def scrapp(cityy):

    urll = requests.get(cityy.url)
    soup = BeautifulSoup(urll.content, 'html.parser')
    week = soup.find(id='seven-day-forecast-body')
    start_date = None
    time_full_rows = soup.find(id='about_forecast').find_all(class_="fullRow")
    for row in time_full_rows:
        if "Forecast Valid" in row.find(class_="left").get_text().strip(" "):
            start_range = row.find(class_="right").get_text().split("-")[0]
            print(start_range)
            if "DT" in start_range:
                start_date = datetime.strptime(start_range.split("DT")[1].strip(" "),  "%b %d, %Y")




    items = week.find_all(class_='forecast-tombstone')
    datee = start_date
    for item in items:
        days = item.find(class_="period-name").get_text()
        descss = item.find(class_="short-desc").get_text()
        temperaturee = item.find(class_="temp").get_text()
        city_idd = cityy.id

        with conn:
            c.execute("SELECT * from forecasts where date = :date  and city_id  = :city_id", {'date': datee , 'city_id': city_idd})
            result = c.fetchall()

            print(result)
            if len(result) < 1:
                print(datee,city_idd)

                params = {'day': str(days), 'descs': str(descss), 'temperature': temperaturee, 'city_id': city_idd, 'date' : datee,'created_at': datetime.now() , 'updated_at': datetime.now()}
                c.execute("INSERT INTO forecasts(day,descs,temperature,city_id,date,created_at,updated_at)VALUES(:day,:descs,:temperature ,:city_id, :date,:created_at,:updated_at)", params)


            else:
                c.execute("UPDATE forecasts SET day=?,descs=?,temperature=? ,city_id=?, date=?,created_at=?,updated_at=? where date = ?  and city_id  = ? ",(str(days),str(descss),temperaturee,city_idd,datee,datetime.now(),datetime.now(),datee,city_idd ))

            datee  = datee + timedelta(days=1)

#
# #
# with conn:
#     c.execute("SELECT * FROM cities")
#     cities_data = c.fetchall()
#     for data in cities_data:
#         city = City(data[2], data[0], data[1])
#         scrapp(city)

#
# c.execute("""CREATE TABLE userdata(
#              ID INTEGER PRIMARY KEY AUTOINCREMENT,
#              Name text,
#              Username text INTEGER,
#              Email text INTEGER,
#              Password text real
#             )""")

# c.execute("DROP TABLE userdata")


#
# # #
# c.execute("""CREATE TABLE cities(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nameofcity text,
#                  url text real
#                 )""")


# #
# # #







































# with conn:
# # c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_1.id,'nameofcity':City_1.name,'url': City_1.url})
#     c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_2.id,'nameofcity':City_2.name,'url': City_2.url})
#     c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_3.id,'nameofcity':City_3.name,'url': City_3.url})
# # c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_4.id,'nameofcity':City_4.name,'url': City_4.url})
#     c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_5.id,'nameofcity':City_5.name,'url': City_5.url})
# # c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url)",{'id':  City_6.id, 'nameofcity':City_6.name,'url': City_6.url})
# # c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_7.id ,'nameofcity':City_7.name,'url': City_7.url})
#     c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_8.id ,'nameofcity':City_8.name,'url': City_8.url})
# # c.execute("INSERT INTO cities(id,nameofcity,url)VALUES(:id ,:nameofcity,:url )",{'id': City_9.id ,'nameofcity':City_9.name,'url': City_9.url})
# with conn:
#     # c.execute("DROP TABLE  forecasts")
#     c.execute("""CREATE TABLE forecasts(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 city_id INTEGER,
#                 day text,
#                 temperature real,
#                 descs text,
#                 date datetime,
#                 created_at  text integer,
#                 updated_at  text integer
#                )""")






conn.commit
conn.close()





























# urls = [ #'https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567',
#         'https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977',
#         'https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453',
#         'https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324',
#         'https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196',
#         #'https://forecast.weather.gov/MapClick.php?lat=30.2676&lon=-97.743',
#         #'https://forecast.weather.gov/MapClick.php?lat=32.7157&lon=-117.1617',
#         'https://forecast.weather.gov/MapClick.php?lat=29.7608&lon=-95.3695',
#         'https://forecast.weather.gov/MapClick.php?lat=39.74&lon=-104.992',
#         'https://forecast.weather.gov/MapClick.php?lat=42.3317&lon=-83.048',
#         ]
# for url in urls:
#
#
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     week = soup.find(id='seven-day-forecast-body')
#     items = week.find_all(class_='forecast-tombstone')
#     for item in items:
#         days = item.find(class_="period-name").get_text()
#         descss = item.find(class_="short-desc").get_text()
#         #temperaturee = item.find(class_="temp").get_text()
#         print(days)
#         print(descss)
#         #print(temperaturee)
#         #c.execute("INSERT INTO forecast(day,descs,created_at,updated_at)VALUES(:dayyyy,:descs,:created_at,:updated_at)",{'dayyyy': str(days) ,'descs': str(descss),'created_at' : ('now') ,'updated_at' : 'now' })
#
# #City _1 = city_data('https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567',1,'MIAMI'),
# City_2 = city_data('https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977',2,'BOSTON')
# City_3 = city_data('https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453',3,'LOS ANGELES')
# #City_4 = city_data('https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324',4,'CHICAGO'),
# City_5 =city_data('https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196',5,'SAN FRANCISCO')
# #City_6 = city_data('https://forecast.weather.gov/MapClick.php?lat=30.2676&lon=-97.743',6,'SAN DIEGO'),
# #City_7 = city_data('https://forecast.weather.gov/MapClick.php?lat=32.7157&lon=-117.1617',7,'HOUSTON'),
# City_8 = city_data('https://forecast.weather.gov/MapClick.php?lat=39.74&lon=-104.992',8,'DENVER')
# #City_9 = city_data('https://forecast.weather.gov/MapClick.php?lat=42.3317&lon=-83.048',9,'DETROIT'),
#



#




# city_1 = CITIESs('BOSTON',58954,'US')
# city_2 = CITIESs('MIAMI',55888,'US')
# city_3 = CITIESs(' ANGELESLOS',54454,'US')
# city_4 = CITIESs('CHICAGO',78554,'US')
# city_5 = CITIESs('SAN FRANCISCO ',87454,'US')
# city_6 = CITIESs('SAN DIEGO',57954,'US')
# city_7 = CITIESs('HOUSTON',78454,'US')
# city_8 = CITIESs('DENVER',12454,'US')
# city_9 = CITIESs('DETROIT',97454,'US')
















# print(city1.name)
# scrapp(City_data1)
# print('---------------------------------------------------------------')
# scrapp(City_data2)


