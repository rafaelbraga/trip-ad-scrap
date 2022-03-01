
from importlib.resources import path
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')

def verifyFirstAccess(wd):
    sleep(3)
    try:
        wd.find_element(By.XPATH,'/html/body/div[10]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[1]/button').click()
    except: 
        print("Botao Cookies não encontrado")
    sleep(50)

if __name__ == "__main__":
    wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wd.get('https://www.tripadvisor.com.br/Restaurants-g303293-Fortaleza_State_of_Ceara.html')
    verifyFirstAccess(wd)


