from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Infow4:
    def __init__(self):
        chrome_options = Options()
        service = Service(executable_path="C:/Windows/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        
    def get_info(self, query):
        self.driver.get(url="https://www.wikipedia.com")
        search_box = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search_box.click()
        search_box.send_keys(query)
        enter= self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button' )
        enter.click()



