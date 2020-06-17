# def scrapp(city):
#     self.url = url
#     page = requests.get(url)
#     soup = BeautifulSoup(url.content, 'html.parser')
#     # print(soup.prettify())
#
#     week = soup.find(id='seven-day-forecast-body')
#     items = week.find_all(class_='forecast-tombstone')
#
#     for item in items:
#         day = item.find(class_="period-name").get_text()
#         desc = item.find(class_="short-desc").get_text()
#         temperature = item.find(class_="temp").get_text()
#         city_id = 2

# class CITIESs:
#     def __init__(self,name,zipcode,country)
import sqlite3
conn = sqlite3.connect('testt.db')
c = conn.cursor()


# c.execute("""CREATE TABLE xyz(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name text,
#             roll_no integer




       #      )""")
c.execute("INSERT INTO xyz VALUES (1 , 'JAzy' , 188)")
# c.execute('DROP TABLE xyz')



conn.commit()
conn.close()