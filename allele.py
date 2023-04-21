
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# import chrome driver
s = Service('C:/Users/HP/Documents/chromedriver_win32/chromedriver.exe')

driver = webdriver.Chrome(service = s)
# hit on page
driver.get('http://www.allelefrequencies.net/pop6001b.asp?pop_polyreg=HLA&pop_type_data=&pop_geog_region=South+Asia')
time.sleep(1)
## retrive html page
html = driver.page_source
with open("allel_links.html","w",encoding="utf-8") as f:
    f.write(html)