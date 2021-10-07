# //*[@id="search"] # 크롬 Copy > X path 로 붙여 넣은 값 사용
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.youtube.com/")

time.sleep(3)
# 검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//input[@id="search"]')
# search = driver.find_element_by_name("search_query")

# 위 search 변수에 값을 전송
search.send_keys('kpop dance cover')
time.sleep(1)
search.send_keys(Keys.ENTER)