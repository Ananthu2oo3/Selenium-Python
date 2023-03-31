from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.marvelmatrimony.com/search/viewuser/5292")
    
pag.write('1111111111')
pag.press('enter')
pag.write('12345678')
pag.press('enter')

for i in range(1,5):
    driver.get(f'https://www.marvelmatrimony.com/search/response?fromyear=26&toyear=30&mothertongue=349&maritalstatus=000&caste=000&page={i}')

    people=driver.find_elements(By.XPATH, "//a[@style='color:#FFF']")

    for i in people:
        links = i.get_attribute('href')
        file = open('links.csv','a')
        file.write(f'{links}\n')
