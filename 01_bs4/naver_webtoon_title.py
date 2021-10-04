from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
# 작업1: [월요 웹툰영역 find] - [해당영역제목 findAll] - [for 문 text 추출]
html = requests.get("https://comic.naver.com/webtoon/weekday")
# pprint(html.text)
soup = bs(html.text, 'html.parser')
html.close()
# pprint(soup)
data1 = soup.find('div',{'class':'col_inner'})# find 는 여러개중 제일 처음 개체만
# pprint(data1)
# 제목포함 영역 추출
data2 = data1.findAll('a',{'class':'title'})
# pprint(data2)
# 텍스트만 추출
# title_list = [] # 배열 자료형 생성
# for t in data2:
#     title_list.append(t.text)
title_list = [t.text for t in data2] # 위 3줄 1줄로 변경
pprint(title_list)
# 작업2: [요일별 웹툰영역 findAll] - [해당영역제목 findAll] - [for 문 text 추출]
data1_list = soup.findAll('div',{'class':'col_inner'})# findAll 은 여러개 모는 개체
pprint(len(data1_list))
# 전체 웹푼 리스트 변수 생성
week_title_lsit = []
# 제목포함 영역 추출
for data1 in data1_list:
    data2 = data1.findAll('a',{'class':'title'})
    # pprint(data2)
    # 텍스트만 추출
    title_list = [t.text for t in data2]
    # pprint(title_list)
    week_title_lsit.append(title_list)
    # 1개 리스트로 합치기(아래)
    # week_title_lsit.extend(title_list)

pprint(week_title_lsit)
# 월요 웹툰만
pprint(week_title_lsit[0])

# 위 전체 웹툰 가져오기를 간단하게 만들기(아래)
html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = bs(html.text, 'html.parser')
html.close()
data1 = soup.findAll('a', {'class':'title'})
week_title_list = [t.text for t in data1]
pprint(week_title_lsit[0])
