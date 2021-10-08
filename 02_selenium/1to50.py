# 1 to 50 웹게임을 자동화 해서 실행하는 파이썬 프로그램
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
driver.get("https://zzzscore.com/1to50/")
driver.implicitly_wait(300)

# 전역변수: 버튼에 매핑되는 현재 숫자
num = 1
def clickBtn(): # 함수생성
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
    # print(len(btns))
    # print(btns[0].text)
    for btn in btns:
        # if btn.text == "1":
        print(btn.text, end='\t')
        if btn.text == str(num):
            btn.click()
            print(True)
            num = num + 1
            return # 함수종료
# 메인실행
while num<=50:
    clickBtn()