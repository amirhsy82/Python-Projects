# Bama website - extracting car names, prices, cities and mileages

# Creating Database
import mysql.connector
cnx = mysql.connector.connect(user='root', password=''
                              host='localhost')

cursor = cnx.cursor()
cursor.execute("CREATE DATABASE Bama")
cursor.execute("CREATE TABLE Car(Name VARCHAR(120), Model VARCHAR(30), Price VARCHAR(30), Mileage VARCHAR(30), City VARCHAR(30)")

# Sending Request to bama.ir 
import requests
from bs4 import BeautifulSoup

Type = str(input("Do you mind a special CarType?(YES/NO)"))
if Type == "YES":
    Type = str(input("Which one?\n ~passenger_car \n ~suv \n ~hatchback \n ~pickup \n ~coupe \n ~convertible \n ~van \n"))
    Url = 'https://bama.ir/car?body=' + Type
    req = requests.get(Url)
    soup = BeautifulSoup(req.text, 'html.parser')
else:
    Class = str(input("Choose Your Car Class:\n (Write in English, example: transmission=automatic or installment=1) \n mileage=0 (کارکرد صفر کیلومتر) \n mileage=1 (کارکرده) \n installment=1 (اقساطی) \n transmission=automatic (اتوماتیک) \n special=offroad \n fuel=hybrid (هیبریدی) \n special=collectable (کلاسیک) \n fuel=cng_gasoline (دوگانه‌سوز) \n None \n "))
    if Class == "None"
        Brand = str(input("Search Your Car:\n( example: peugeot-207 )\n"))
        Url = 'https://bama.ir/car/' + Brand
        req = requests.get(Url)
        soup = BeautifulSoup(req.text, 'html.parser')
    else:
        Url = 'https://bama.ir/car?' + Class
        req = requests.get(Url)
        soup = BeautifulSoup(req.text, 'html.parser')


# Extracting Car Names
Car_name = soup.find_all('p', attrs={'class':'bama-ad__title'})
Car_list = []
for i in range(100):
    for item in Car_name:
        item = item.text
        Car_list += [item.strip()]


# Extracting Car Models
Model = soup.find_all('span', attrs={'class':'bama-ad__detail-trim'})
Model_list = []
for i in range(100):
    for item in Model:
        item = item.text
        Model_list += [item.strip()]


# Extracting Car Prices
Car_price = soup.find_all('span', attrs={'class':'bama-ad__price'})
Price_list = []
for i in range(100):
    for item in Car_price:
        item = item.text
        Price_list += [item.strip()]

# Extracting Car Mileages
Car_mileage = soup.find_all('div', attrs={'class':'bama-ad__detail-row'})
# Using regex for extracting just The Price
import re
regex = r"\d*,\d*\sکیلومتر"
Mileage_list = []
for i in range(100):
    for item in Car_mileage:
        item = item.text
        mile = re.findall(regex, item)
        Mileage_list += [mile]


# Extracting cities
city = soup.find_all('div', attrs={'class':'bama-ad__address'})
city_list = []
for i in range(100):
    for item in city:
        item = item.text
        city_list += [item.strip()]

# Insert in Database
counter = 0
for item in range(100):
    D = "INSERT INTO car(Name, Model, Price, Mileage, City) Values(%s, %s, %s, %s, %s)"
    val = (Car_list[counter], Model_list[counter], Price_list[counter], Mileage_list[counter], city_list[counter])
    cursor.execute(D, val)
    counter += 1
    cnx.commit()

# Sorting the results Alphabetically by City
sql = "SELECT * FROM Car ORDER BY City"
cursor.execute(sql)
final_result = cursor.fetchall()
for item in final_result:
    print(item)
    
# Selecting the city
City = str(input("Which City do you mind? \n(example:تهران\n"))
Sql = f"SELECT * FROM Car WHERE City = {City}"
cursor.execute(Sql)
result = cursor.fetchall()
for item in result:
    print(item)

# Ordering by Price
Max_Price = int(input("How much does it cost?"))
Max = f"SELECT * FROM Car WHERE Price >= {Max_Price}"
cursor.execute(Max)
res = cursor.fetchall()
if res == "" :
    while res == ""
        print("There isn't any car in your price range!")
        Max_Price = int(input("How much does it cost?"))
        Max = f"SELECT * FROM Car WHERE Price >= {Max_Price}"
        cursor.execute(Max)
        res = cursor.fetchall()

else:
    for item in res:
        print(item)

cnx.close()
