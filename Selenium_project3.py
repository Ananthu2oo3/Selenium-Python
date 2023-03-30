from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://en.wikipedia.org/wiki/Mahatma_Gandhi')

val = driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table/tbody/tr[1]/th/div[2]')
print(val.text)