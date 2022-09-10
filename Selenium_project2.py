"""
Author:Ananthakrishnan G
source link: https://www.whizlabs.com/labs/library
last modified: 
"""
 
from http.server import executable
from statistics import mode
import urllib
from selenium import webdriver
#import pandas as pd 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import json
import csv
 
#pd.options.display.max_columns = None
#pd.options.display.max_rows = None
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
def writeJSONFile(path,filename,data):
    filePathNameWExt='./' + path + './' + filename + '.json' 
    with open(filePathNameWExt,'a') as fp:
        json.dump(data,fp,indent=4)
 
path='./'
 
chrome_options = Options()
chrome_options.add_argument("--headless")
 
def startpy():
    dict_over=[]
    PATH = "/home/ananthu/selenium/chromedriver"
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=PATH)
    driver.maximize_window()
    
    lnk="https://weather.com/en-IN/weather/today/l/13.08,80.27?par=google"
    driver.get(lnk)
    
    #formatted_lnk = lnk.format(start_date.year,start_date.month,start_date.day) 
    location=driver.find_element(By.XPATH,'//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[1]/h1')
    temperature_1=driver.find_element(By.XPATH,'//*[@id="WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034"]/div/section/div/div[2]/div[1]/div[1]/span')
    temperature_2=driver.find_element(By.XPATH,'//*[@id="WxuDailyWeatherCard-main-bb1a17e7-dc20-421a-b1b8-c117308c6626"]/section/div/ul/li[2]/a/div[1]/span')
    temperature_3=driver.find_element(By.XPATH,'//*[@id="WxuDailyWeatherCard-main-bb1a17e7-dc20-421a-b1b8-c117308c6626"]/section/div/ul/li[3]/a/div[1]/span')
 
 
    dict={
            "Location":location.text,
            "Day_1":temperature_1.text,
            "Day_2":temperature_2.text,
            "Day_3":temperature_3.text,
     }
    time.sleep(5)
 
    writeJSONFile(path,"Weather",dict)
    #dict_over.append(dict)



if __name__ == '__main__':
    startpy()
 

