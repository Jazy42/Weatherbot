import sqlite3
from cities import CITIESs

conn = sqlite3.connect('weather.db')
c = conn.cursor()
#c.execute("""CREATE TABLE CITIES(
 #           cityid integer  PRIMARY KEY AUTOINCREMENT,
  #          nameofcity text,
   #         zipcode integer,
    #       country text
     #       )""")
#c.execute("DROP TABLE CITIES")
#c.execute("INSERT INTO CITIES VALUES(1 , 'MIAMI' ,55621,'US','now','now' )")
#c.execute("SELECT * FROM CITIES")
#print(c.fetchall())

#c.execute("""CREATE TABLE FORECAST(
 #               id INTEGER PRIMARY KEY,
  #              cityid INTEGER,
   #             day text,
    #            temp real,
     #           desc text,
      #          created at text,
          #      updated at text
           #     )""")
#c.execute("DROP TABLE CITIES")
def insert_city(nameofcity):
    pass
def insert_zipcode(Zipcode):
    pass
def insert_country(country):
    pass















#city_1 = CITIESs('Newyork',58954,'US')
#city_2 = CITIESs('Florida',58854,'US')
#city_3 = CITIESs('Boston',57454,'US')
#c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_1.name , 'Zipcode':city_1.Zipcode,'country':city_1.country})
#c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_2.name , 'Zipcode':city_2.Zipcode,'country':city_2.country})
#c.execute("INSERT INTO CITIES(nameofcity,zipcode,country) VALUES(:name,:Zipcode,:country )",{'name': city_3.name , 'Zipcode':city_3.Zipcode,'country':city_3.country})


c.execute("SELECT * FROM CITIES")
print(c.fetchall())


conn.commit()
conn.close()