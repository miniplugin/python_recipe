import errno
import os.path
from urllib.request import urlretrieve
import re
import requests
from bs4 import BeautifulSoup as bs

# 웹 페이지를 열고 소스코드를 읽어보는 작업
html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = bs(html.text, 'html.parser')
html.close()

# 요일별 웹툰영역 추출하기
detail_list = soup.findAll('div',{'class':'col_inner'})
# pprint(detail_list)

# 전체 웹툰 리스트
li_list = []
for data1 in detail_list:
    # 제목+썸네일 영역 추출
    li_list.extend(data1.findAll('li'))
# pprint(li_list)

# 저장할 폴더 생성
try:
    if not (os.path.isdir('download')):
        os.makedirs(os.path.join('download'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생생 실패!")
        exit;

# 각각 thumb>img>src, title : 썸네일과 제목 추출하기 후 download 폴더에 저장
for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    print(title,img_src)
    title = re.sub('[^0-9a-zA-Zㄱ-힗]','',title)
    urlretrieve(img_src, './download/' + title + '.jpg')