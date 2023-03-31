from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
import json
import time

def startpy():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.marvelmatrimony.com/search/viewuser/5292")
        

    pag.write('1111111111')
    pag.press('enter')
    pag.write('12345678')
    pag.press('enter')


    file = open('links.csv', 'r')
    time.sleep(3)
    for link in file:
        driver.get(link)

        # print((({driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/h4')).text).text)

        dict = {
        # #basic details
            "name"                : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/h4')).text,
            "age "                : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[1]/div[2]')).text,  
            "gender "             : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[1]/div[4]')).text,
            "children "           : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[2]/div[2]')).text,
            "phgysical_challenge" : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[3]/div[2]')).text,
            "marital_status"      : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[3]/div[4]')).text,
            "mother_tongue"       : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[4]/div[2]')).text,
            
        # RELIGIOUS INFORMATION
            "relegion"            : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[1]/div[2]').text),
            "caste"               : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[1]/div[4]').text),
            "denamonation"        : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[2]/div[2]').text),
            "curch"               : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[2]/div[4]').text),
            "belief_type"         : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[3]/div[2]').text),
            "baptized"            : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[3]/div[4]').text),
            "curch_membership"    : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[4]/div[2]').text),
            "jewellery"           : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[5]/div[4]/div[4]').text),
        
        # LIFESTYLE
            "eating_habbits"      : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[7]/div[2]/div[2]').text),
            "height"              : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[5]/div[2]').text),
            "weight"              : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[5]/div[4]').text),
            "complextion"         : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[4]/div[4]').text),
            "body_type"           : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[3]/div[2]/div[4]').text),
            "drinking"            : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[7]/div[1]/div[2]').text),
            "smoking"             : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[7]/div[1]/div[4]').text),
            
        # PROFESSIONAL INFORMATION
            "education"           : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[9]/div[1]/div[2]').text),
            "employment"          : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[9]/div[1]/div[4]').text),
            "industry"            : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[9]/div[2]/div[2]').text),
            "annual_income"       : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[9]/div[2]/div[2]').text),
            "experience"          : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[9]/div[3]/div[2]').text),
            "location"            : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[9]/div[3]/div[4]').text),

        # FAMILY DETAILS
            "family_type"         : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[11]/div[1]/div[2]').text),
            "status"              : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[11]/div[1]/div[4]').text),
            "brothers"            : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[11]/div[2]/div[2]').text),
            "sisters"             : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[11]/div[2]/div[4]').text),
            
        # PARTNER PREFERENCE

            "inter_cast"          : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[1]/div[2]').text),
            "prefered_caste"      : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[1]/div[4]').text),
            "prefered_denominant" : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[2]/div[4]').text),
            "inter_denomination"  : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[2]/div[2]').text),
            "patner_education"    : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[3]/div[2]').text),
            "work_willingness"    : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[4]/div[2]').text),
            "patner_age"          : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[4]/div[4]').text),
            "patner_height"       : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[5]/div[2]').text),
            "patner_complextion"  : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[5]/div[4]').text),
            "patner_jewelllery"   : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[6]/div[2]').text),
            "patner_occupation"   : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[6]/div[4]').text),
            "patner_relegion"     : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[7]/div[2]').text),
            "patner_worktype"     : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[7]/div[4]').text),
            "within_state"        : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[8]/div[2]').text),
            "abroad"              : (driver.find_element(By.XPATH,'//*[@id="app2s"]/div/div/div/div/div/div[13]/div[8]/div[4]').text)
        }

        # lst = list(dict)
        # # time.sleep(3)
        # ab = dict["height"]
        # print("data")
        # print(ab)

        with open ('user_data.json','a+') as f:
            json.dump(dict,f,indent=4)
        
    

if __name__ == '__main__':
    startpy()