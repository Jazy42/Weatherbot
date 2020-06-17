#import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
import 
from forcecat import Forecast
sqlite3
conn = sqlite3.connect('weather.db')
c = conn.cursor()
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=25.7748&lon=-80.1977')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')

items =  week.find_all(class_='tombstone-container')

#period_names = [item.find(class_='period-name').get_text() for item in items]
#short_descriptions = [item.find(class_='short-desc').get_text() for item in items]
#temperatures = [item.find(class_='temp').get_text() for item in items]
forecasts = []
for item in items:
    day = item.find(class_="period-name").get_text()
    desc = item.find(class_="short-desc").get_text()
    temperature = item.find(class_="temp").get_text()
    city_id = 1
    f = Forecast(day=day, desc=desc, temperature=temperature, city_id=city_id)
    forecasts.append(f)

for forecast in forecasts:
    c.execute("""   
    INSERT INTO forecasts(city_id, day, desc, temperature, created_at, updated_at) VALUES(:city_id, :day, :desc, :temp,datetime('now'),datetime('now'))
    """,{
        'city_id': forecast.city_id,
        'day': forecast.day,
        'desc': forecast.desc,
        'temp': forecast.temperature
    })

conn.commit()
conn.close()










































#MYDICT = [{'DAYS' : period_names , 'DESC' : short_descriptions , 'TEMP' : temperatures}]
#forceast = Forecast(day=period_names, desc=short_descriptions, temperature=temperatures)

#print(MYDICT)
#y = json.dumps(MYDICT)
#print(y)




















#weather_stuff = pd.DataFrame(
    #{
        #'Day': period_names,
        #'Description': short_descriptions,
        #'temp': temperatures,
    #})
#print(weather_stuff)
#weather_stuff.to_csv('weather.csv')\\\










































































#articles = soup.find(id='waitDiv')
#print(articles.prettify())
#items = articles.find(class_='ge gf r')
#print(items.prettify())
#content = items.find_all(class_='gg gh ai gi r gj gk gl gm gn')
#print(content[0].find(class_='ap q ec bw ed bx fh gw gx as av fi ei ej au').get_text()) #title
#print(content[0].find(class_='bw b bx by bz ca as av el ei ej au ap q').get_text())   #Nameofwriter
#print(content[0].find(class_='ft n co').get_text())  #dateandminread
#Title_name = [contents.find(class_='ap q ec bw ed bx fh gw gx as av fi ei ej au').get_text() for contents in content]
#Name_of_writer=[contents.find(class_='bw b bx by bz ca as av el ei ej au ap q').get_text() for contents in content]
#date_andmin_read = [contents.find(class_='ft n co').get_text() for contents in content]
#print(Title_name)
#print(Name_of_writer)
#print(date_andmin_read)


#mediumdataa = [{'title' : Title_name , 'Author' : Name_of_writer, 'Dateandtime' : date_andmin_read }]
#print(mediumdataa[0])


#y = json.dumps(mediumdataa)
#print(y)





























