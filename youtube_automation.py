from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Infow:
    def __init__(self):
        chrome_options = Options()
        service = Service(executable_path="C:/Windows/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
    
    def play(self, query):
        self.query= query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        enter= self.driver.find_element(By.XPATH,'//*[@id="video-title"]')
        enter.click()
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, 'html5-video-player'))
            )
