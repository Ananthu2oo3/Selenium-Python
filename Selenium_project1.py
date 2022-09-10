"""
Author:Bagiya Lakshmi S, Ananthakrishnan G
source link: https://www.whizlabs.com/labs/library
last modified: 18.08.2022
"""




from http.server import executable
from statistics import mode
import urllib
from selenium import webdriver
import pandas as pd 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import json
import csv
 
def writeJSONFile(path,filename,data):
    filePathNameWExt='./' + path + './' + filename + '.json' 
    with open(filePathNameWExt,'a') as fp:
        json.dump(data,fp,indent=4)
 
path='./'
 
with open('links.csv', newline='') as f:
    reader = csv.reader(f)
    data_1 = list(reader)



chrome_options = Options()
chrome_options.add_argument("--headless")



def startpy():
    dict_over=[]
    PATH = "/home/ananthu/selenium/chromedriver"
    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=PATH)
    driver.maximize_window()
    for i in data_1:
        driver.get(i[0])
        time.sleep(5)
        title=driver.title
        lab_overview=driver.find_element(By.XPATH,'//*[@class="main-heading"]')
 
        # lnk="https://www.whizlabs.com/labs/configure-email-notification-on-s3-bucket-event-amazon-sns-challenge"
        # driver.get(lnk)
 
        try:
            lab_detail=driver.find_element(By.XPATH,'//*[@class="description-section"]/div[@class="box"]')
            # lab_detail=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[1]')   
            # lab_intr=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ul)')      
            # task=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[2]')
            # lab_env=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[3]')
            # img = driver.find_element_by_xpath('(//*[@class="descri-block"]//img)[1]')
            # src = img.get_attribute('src')
  
 
        
        # pic=pic_lnk.get_attribute('alt src')
            
            dict={
                 "title":title,
                 "lab_overview":lab_overview.text,
            #     "lab_intro":lab_intr.text,
                 "lab_detail":lab_detail.text,
            #     "task":task.text,
            #     "lab_env":lab_env.text,
            #     "pic":src
 
             }
            time.sleep(5)
 
            dict_over.append(dict)
        except Exception as e:
            print(e)
            preques=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[1]')
            challenge_inst=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[2]')
            sub_env=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[3]')
            launch_env=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[4]')
            dict={
                "title":title,
                "lab_overview":lab_overview.text,
                "preques":preques.text,
                "challenge_inst":challenge_inst.text,
                "sub_env":sub_env.text,
                "launch_env":launch_env.text
            }
            time.sleep(5)
            dict_over.append(dict)
            time.sleep(5)
            
        # else:
        #     lab_detail=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[1]')
        #     task=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[2]')
        #     lab_env=driver.find_element(By.XPATH,'(//*[@class="descri-block"]/ol)[3]')
        #     #img = driver.find_element_by_xpath('(//*[@class="descri-block"]//img)[1]')
        #     #src = img.get_attribute('src')
        #     dict={
        #          "title":title,
        #          "lab_overview":lab_overview.text,
        #     #     "lab_detail":lab_detail.text,
        #     #     "task":task.text,
        #     #     "lab_env":lab_env.text,
        #     #     "pic":src
        #      }
        #     time.sleep(5)
        #     dict_over.append(dict)
        #     time.sleep(5)
    writeJSONFile(path,"Whizlabs",dict_over)
        
       
 
if __name__ == '__main__':
    startpy()




