from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time
import pyautogui



FirstName = "Cool"
LastName  ="Kid"

password  ="PROgrammer1"
#Wont work without min. 8 characters, 1 letter , 1 number ,Both upper and lower case

PATH = "chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://email-fake.com/")

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email_ch_text"))
)



zoomdriver = webdriver.Chrome(ChromeDriverManager().install())
zoomdriver.get("https://us04web.zoom.us/signup")

zoomelement = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
)
zoomelement.click()
time.sleep(1)

zoomelement = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.ID, "select-0"))
)
zoomelement.click()
time.sleep(0.6)
month = zoomdriver.find_element(By.ID,"select-item-select-0-0")
month.click()
zoomelement = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.ID, "select-1"))
)
zoomelement.click()
time.sleep(0.6)
day = zoomdriver.find_element(By.ID,"select-item-select-1-0")
day.click()
zoomelement = WebDriverWait(zoomdriver, 10).until(
    EC.presence_of_element_located((By.ID, "select-2"))
)
zoomelement.click()
time.sleep(0.7)
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
flag=False
zoomdriver.quit()

while flag==False:
    #driver.execute_script("window.scrollTo(0,400)") 
    l=driver.find_elements(By.TAG_NAME,"a")
    for i in l:
        try:
            print("\n"+i.text)
            if "https:" in i.text:
                print("There you go:" + i.text)
                zoom = webdriver.Chrome(ChromeDriverManager().install())
                zoom.get(i.text)
                flag=True
                break
        except:
            continue  
        flag+=1      


""" driver.quit()
 """

zoomelement = WebDriverWait(zoom, 10).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
)
print("Cookies accepted")
zoomelement.click()
print("Cookies accepted clicked")

time.sleep(4)
for i in range(15):
    pyautogui.press('tab')

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









