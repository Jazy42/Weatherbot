import sqlite3
from cities import CITIESs

conn = sqlite3.connect('weather.db')
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS cities""")
c.execute("""CREATE TABLE cities(
            cityid integer  PRIMARY KEY AUTOINCREMENT,
            nameofcity text,
            zipcode integer,
           country text
            )""")

c.execute("""DROP TABLE IF EXISTS forecasts""")
c.execute("""CREATE TABLE forecasts(
                id INTEGER PRIMARY KEY,
                city_id INTEGER,
                day text,
                temperature real,
                desc text,
                created_at datetime,
               updated_at datetime
               )""")
#c.execute("DROP TABLE CITIES")
def insert_city(nameofcity):
    pass
def insert_zipcode(Zipcode):
    pass
def insert_country(country):
    pass



city_1 = CITIESs('Newyork',58954,'US')
city_2 = CITIESs('Florida',58854,'US')
city_3 = CITIESs('Boston',57454,'US')
c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_1.name , 'Zipcode':city_1.Zipcode,'country':city_1.country})
c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_2.name , 'Zipcode':city_2.Zipcode,'country':city_2.country})
c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_3.name , 'Zipcode':city_3.Zipcode,'country':city_3.country})

c.execute("SELECT * FROM CITIES")
print(c.fetchall())


conn.commit()
conn.close()

# city_1 = CITIESs('BOSTON',58954,'US')
# city_2 = CITIESs('MIAMI',55888,'US')
# city_3 = CITIESs(' ANGELESLOS',54454,'US')
# city_4 = CITIESs('CHICAGO',78554,'US')
# city_5 = CITIESs('SAN FRANCISCO ',87454,'US')
# city_6 = CITIESs('SAN DIEGO',57954,'US')
# city_7 = CITIESs('HOUSTON',78454,'US')
# city_8 = CITIESs('DENVER',12454,'US')
# city_9 = CITIESs('DETROIT',97454,'US')