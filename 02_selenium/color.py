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

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
# print(len(btns))
# print(btns[0].value_of_css_property('background-color'))

def analysis():
    btns_rgba_list = [btn.value_of_css_property('background-color') for btn in btns]
    # pprint(btns_rgba_list)
    result = Counter(btns_rgba_list) # 카운트 함수는 색상 rgba 값이 몇개씩인지 통계를 구할 수 있다.
    # pprint(result)
    # result 에서 색상 rgba 값이 1인 것 탐색
    for key, value in result.items():
        if value == 1:
            answer = key
            break
        else:
            answer = None
            print("다른 색상을 찾을 수 없습니다.")
    # 해당 색상 클릭: 1. btns_rgba_list 에서 인덱스 값을 구하고 -> 그 인덱스 값으로 btns 를 클릭
    if answer:
        index = btns_rgba_list.index(answer)
        btns[index].click()

# 메인부분 (단, 실행후 배너창을 닫아야 합니다.)
start = time.time()
while time.time() - start <= 60:
    analysis()