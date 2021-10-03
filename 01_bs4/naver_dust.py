from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
# 이 프로그램은 뷰티풀 소프 라는 soup 프로토콜 파싱툴을 이용해서 네이버 미세먼지 크롤링을 하는 실습 입니다.
html = requests.get("https://search.naver.com/search.naver?query=날씨")
# pprint(html.text)
soup = bs(html.text,'html.parser')
# pprint(soup)
data1 = soup.find('ul',{'class':'today_chart_list'})#딕셔너리 자료형으로 class 키:값 지정
# pprint(data1)
data2 = data1.findAll('li')
# pprint(data2[0])
find_dust = data2[0].find('span',{'class':'txt'})
pprint(find_dust.text)