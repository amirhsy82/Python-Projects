import requests 
from bs4 import BeautifulSoup

# Sending Request to Truecar website
Brand = str(input(""))
Url = 'https://www.truecar.com/used-cars-for-sale/listings/' + Brand
r = requests.get(Url)
soup = BeautifulSoup(r.text, 'html.parser')

# import Database
import mysql.connector

cnx = mysql.connector.connect(user ="root", password ="",
                              host ="localhost")

cursor = cnx.cursor()
cursor.execute("CREATE DATABASE truecar")
cursor.execute("CREATE TABLE car(Car VARCHAR(100), Price Varchar(20), Mileage Varchar(20)")

# Extracting car's name
Car_name = soup.find_all('div', attrs={'class':'vehicle-card-top'})
Car_list = []
counter = 0
while counter != 21:
    for item in Car_name :
        Car_list += [item.text]
        counter += 1

# Extracting car's price
Car_price = soup.find_all('div', attrs={'class':'vehicle-card-bottom vehicle-card-bottom-top-spacing'})

# Using regex for extracting just The Price
import re
regex = r"list price(\$\d.*)"

Price_list = []
counter = 0
while counter != 21:
    for item in Car_price:
        item = item.text
        price = re.findall(regex, item)
        Price_list += price
        counter +=1

# Extracting car's mileage
Car_mileage = soup.find_all('div', attrs={'class':'mt-2-5 w-full border-t pt-2-5'})
regex = r"\d.*miles"
Mileage_list = []
counter = 0
while counter != 21:
    for item in Car_mileage:
        item = item.text
        mile = re.findall(regex, item)
        Mileage_list += mile
        counter +=1

# Inserting in Database
counter = 0
for item in range(21):
    D = "INSERT INTO car(Car, Price, Mileage) Values(%s, %s, %s)"
    val = (Car_list[counter], Price_list[counter], Mileage_list[counter])
    cursor.execute(D, val)
    counter += 1
    cnx.commit()






