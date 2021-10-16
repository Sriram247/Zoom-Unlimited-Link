from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time
import pyautogui



FirstName "Cool"
LastName  ="Kid"

password  ="PROgrammer1"
#Wont work without min. 8 characters, 1 letter , 1 number ,Both upper and lower case

PATH = "msedgedriver.exe"
driver = webdriver.Edge(PATH)


driver.get("https://email-fake.com/")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email_ch_text"))
)



zoomdriver = webdriver.Edge(PATH)
zoomdriver.get("https://us04web.zoom.us/signup")



zoomelement = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.ID, "select-0"))
)
zoomelement.click()
time.sleep(0.2)
month = zoomdriver.find_element(By.ID,"select-item-select-0-0")
month.click()
zoomelement = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.ID, "select-1"))
)
zoomelement.click()
time.sleep(0.2)
day = zoomdriver.find_element(By.ID,"select-item-select-1-0")
day.click()
zoomelement = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.ID, "select-2"))
)
zoomelement.click()
time.sleep(0.2)
year = zoomdriver.find_element(By.ID,"select-item-select-2-99")
year.click()


button = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "zm-button__slot"))
)
button.click()


text = element.text

pyautogui.write(text,interval='0.05')

#remember to change enter to selenium
pyautogui.press('enter')



#activate = WebDriverWait(driver, 12).until(
#    EC.presence_of_element_located((By.LINK_TEXT, "Please activate your Zoom..."))
#)
#activate.click()
time.sleep(1)
driver.refresh()
flag=0
zoomdriver.quit()

while flag<25:
    #driver.execute_script("window.scrollTo(0,400)") 
    l=driver.find_elements(By.TAG_NAME,"a")
    for i in l:
        try:
            print("\n"+i.text)
            if "https:" in i.text:
                print("There you go:" + i.text)
                zoom = webdriver.Edge(PATH)
                zoom.get(i.text)
                flag=25
                break
        except:
            continue  
        flag+=1      


driver.quit()

pyautogui.write(FirstName,interval='0.05')
pyautogui.press('tab')
pyautogui.write(LastName,interval='0.05')
pyautogui.press('tab')
pyautogui.write(password,interval='0.05')
pyautogui.press('tab')
pyautogui.write(password,interval='0.05')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(6)
for i in range (8):
    pyautogui.press('tab')
pyautogui.press('enter')

A = input("\n\nPress enter to close....")  









