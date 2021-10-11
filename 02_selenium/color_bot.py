from selenium import webdriver
from pprint import pprint
from collections import Counter
import time

# 색감 테스트: 주어진 시간안에 다른 색을 선택하기 //*[@id="grid"]/div[1]
driver = webdriver.Chrome('chromedriver')
driver.get('http://zzzscore.com/color/')
driver.implicitly_wait(300)

# description element 까지 스크롤
# driver.execute_script('window.scrollTo(0, document.querySelector("#grid").offsetHeight)')
temp = '''
    var location = document.querySelector("#grid").offsetHeight;
    window.scrollTo(0, location);
'''
driver.execute_script(temp)
# 메인부분 (단, 실행후 배너창을 닫아야 합니다.)
start = time.time()
while time.time() - start <= 60:
    try:
        btn = driver.find_element_by_class_name("main")
        btn.click()
    except:
        pass