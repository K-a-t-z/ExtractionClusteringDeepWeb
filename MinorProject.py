from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox()

driver.get("https://www.nobroker.in/chennai/rent")

localities = [
    'Nungambakkam' ,
    'Adyar' ,
    'Anna Nagar' ,
    'Egmore' ,
    'Kilpauk' ,
    'Alwarpet' ,
    'Royapettah' ,
    'Besant Nagar' ,
    'Kotturpuram' ,
    'Tambaram' ,
    'Velachery' ,
    'Vadapalani' ,
    'Chetpet' ,
    'Mylapore' ,
    'Urapakkam' ,
    'Ambattur' ,
    'Alandur' ,
    'Guindy' ,
    'Ashok Nagar' ,
    'Saidapet' ,
    'Perungudi' ,
    'Thoraipakkam' ,
    'Triplicane' ,
    'Thiruvanmiyur' ,
    'Washermanpet' ,
    'Taramani' ,
    'Madhavaram' ,
    'Shenoy Nagar' ,
    'Teynampet' ,
    'West Mambalam' ,
    'Koyambedu' ,
    'Ramapuram' ,
    'Meenambakkam' ,
    'Kelambakkam' ,
    'Vandalur' ,
    'Nandanam' ,
    'Sowcarpet' ,
    'Porur' ,
    'Saligramam' ,
    'TNagar' ,
    'Neelankarai' ,
    'Kottivakkam'
    ]

HEADER = ['Areas' , 'Rents']
DATA = []

random.shuffle(localities)

# for i in range (3) :
for i in range (len(localities)) :

    try :

        time.sleep(0.2)

        driver.find_element("id" , "listPageSearchLocality").send_keys(localities[i])

        time.sleep(0.2)

        driver.find_element("id" , "listPageSearchLocality").click()

        time.sleep(0.2)

        driver.find_element("id" , "listPageSearchLocality").send_keys(Keys.ARROW_DOWN)

        time.sleep(0.2)

        driver.find_element("id" , "listPageSearchLocality").send_keys(Keys.ENTER)

        time.sleep(1)

        driver.find_element("css selector" , "button.prop-search-button").click()

        time.sleep(3)

        find_area = driver.find_elements("xpath" , "//*[@id = 'unitCode']")
        areas = [x.get_attribute("innerHTML") for x in find_area]
        areas = [''.join(a.split(' sqft')[0].split(',')) for a in areas]

        find_rent = driver.find_elements("xpath" , "//*[@id = 'minimumRent']")
        rents = [x.get_attribute("innerHTML")[:9] for x in find_rent]
        rents = [r[:r.rfind("0")+1] if r.rfind("0") != -1 else " 0" for r in rents]
        rents = [''.join(r.split(' ')[1].split(',')) for r in rents]

        for x in range (len(areas)) :
            DATA.append([areas[x] , rents[x]])

        time.sleep(0.2)

        driver.back()

        time.sleep(0.2)

        driver.find_element("id" , "listPageSearchLocality").send_keys(Keys.BACKSPACE)
    
    except :

        print("Uh-oh! Something went wrong :(")

# print(DATA)

with open ('data1.csv' , 'w') as file1 :
    file1.write(','.join(HEADER))
    file1.write('\n')
    for row in DATA :
        file1.write(','.join(row))
        file1.write('\n')

time.sleep(1)

driver.close()