from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import csv


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser = webdriver.Chrome("/Users/shenayaverma/Desktop/python/scraper/chromedriver")

browser.get(START_URL) 

time.sleep(10)
def scrape():
    headers = ['NAME',' LIGHT-YEARS FROM EARTH ', 'PLANET MASS	', ' STELLAR MAGNITUDE	', 'DISCOVERY DATE']
    planet_data = []
    for i in range(0,4):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for a in soup.find_all('ul',attrs={"class", "exoplanet"}):
            print(a.contents[0])

scrape()
