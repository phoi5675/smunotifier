#-*- coding:utf-8 -*-
import requests
from datetime import date
from bs4 import BeautifulSoup
import const
class board():
    def __init__(self, title, date, board_id, board_name):
        self.title = title
        self.date = date
        self.board_id = board_id
        self.board_name = board_name
def scrap(web_index, board_name, mlist):
    '''
    사이트에서 게시물 추출하는 부분
    '''
    # request web addr and prettify html
    r = requests.get(web_index)
    res = r.text

    #res.lstrip()

    res = res.replace("\t", "")
    res = res.replace("\n", "")
    res = res.replace("\r", "")

    soup = BeautifulSoup(res, 'lxml')
    #soup.prettify()

    has_noti = 0 # 공지가 존재하는지 확인하는 변수

    '''
    게시물의 각 제목은 <tbody> 태그 내의 <tr> 태그로 감싸져 있으므로
    <tbody> 를 먼저 뽑아낸 후, 각각 게시물의 (타이틀 / id(링크) / 날짜)를 추출 후, 오늘 날짜와 일치하는지 확인
    오늘 날짜와 일치하는 경우만 리스트에 뽑음
    '''
    ul = soup.find("ul", class_='board-thumb-wrap')
    dl_list = ul.find_all('dl')
    for dl in dl_list:
        # 타이틀 추출
        # 학과 게시판은 [천안], [서울], 등의 지역과 카테고리가 없고, 전체 공지는 있으므로 try / except 사용
        try:
            region = dl.find('span', class_='cmp').get_text()
            cate = dl.find('span', class_='cate').get_text()
            xml_title = dl.find('a').span.clear()
            title = xml_title.get_text()

            temp_title = region + cate + title
        except:
            temp_title = dl.find('a').get_text()
        # 게시물 날짜 추출
        date_xml = dl.find('li', class_='board-thumb-content-date')
        date_xml.span.clear()
        temp_date = date_xml.get_text()
        # 게시물 id 추출
        temp_id = web_index +  dl.a.get('href')
        # 오늘 날짜와 일치하는 경우, 리스트에 추가
        if temp_date == today:
        #if temp_date == '2020-05-06': # 테스트용
            mlist.append(board(temp_title, temp_date, temp_id, board_name))
            has_noti += 1
    if has_noti > 0:
        return 1
    else:
        return 0

# 학부 / 학과별 공지를 저장할 배열
gen_list = list(list() for i in range(len(const.SMUARY)))
dept_list = list(list() for i in range(len(const.DEPARY)))

gen_noti_count = 0 # 일반 공지 전체 카운트 변수
dept_noti_count = list(0 for i in range(len(const.DEPARY))) # 학부별 공지 카운트 변수

# 오늘 날짜 확인
today = date.today().isoformat()
file_out = []

# 일반공지
for gen_web_index, gen_index, gen_list_index in zip(const.SMUARY, const.GENFIARY, gen_list):
    # 오늘의 학교 홈페이지 공지사항을 gen_list 에 저장
    if scrap(gen_web_index, const.GENFIARY, gen_list_index):
        gen_noti_count += 1

# 각 학과별 학과공지
for dept_web_index, dept_noti_index, dept_index in zip(const.DEPARY, const.DEPFIARY, dept_list):
    # 오늘의 학과 공지사항을 dept_list 에 저장
    if scrap(dept_web_index, dept_noti_index, dept_index):
        dept_noti_count[const.DEPARY.index(dept_web_index)] += 1

# 파일로 내보내기
html_text = '''
<!DOCTYPE html>
<html>

<head>
    <meta charset=\"utf-8\">
    <title>SMU Notifier</title>
</head>

<body>
    <h1>상명대학교 공지사항</h1><br>
    <h2>일반공지<br></h2>
        <div class="general"></div>
    <h2>학과공지<br></h2>
        <div class="dept"></div>
    <p>구독을 중단하고 싶은 경우<br>phoiSMUNotifier@gmail.com<br>으로 메일을 보내주시기 바랍니다.</p>
</body>

</html>'''
for dept_index, dept_file, dept_noti_count_index in zip(dept_list, const.DEPFIARY, dept_noti_count):
    html_base = BeautifulSoup(html_text, 'lxml')
    # 공지를 html 에 추가하는 부분을 함수로 만들면 훨씬 코드가 깔끔하겠지만 그냥 쓰자
    # 일반공지 먼저 추가
    for gen_index in gen_list:
        for i in range(0, len(gen_index)):
            div = html_base.find(class_="general")

            # 타이틀과 링크를 추가
            new_tag = html_base.new_tag('a', href=gen_index[i].board_id)
            new_tag.string = gen_index[i].title
            new_tag.append(html_base.new_tag("br"))
            div.insert_after(new_tag)

    # 학과공지 추가
    # 학과 공지 개수가 1개 이상일 수 있으므로 루프를 하나 더 생성해서, 학과 공지 "목록"을 html 에 추가
    if dept_noti_count_index != 0:
        for i in range(0, len(dept_index)):
            # 학과 공지글이 없는 경우, 과정 생략
            div = html_base.find(class_="dept")

            # 타이틀과 링크를 추가
            new_tag = html_base.new_tag('a', href=dept_index[i].board_id)
            new_tag.string = dept_index[i].title
            new_tag.append(html_base.new_tag("br"))
            div.insert_after(new_tag)
    if (dept_noti_count_index != 0) or (gen_noti_count != 0):
        # 파일에 저장하기 / 왜 with open 은 오류가 나는건지?`
        # 학교 / 학부 공지 중 하나 이상이 존재하는 경우에만 파일 생성
        fi = open(const.FILEPATH + 'html/' + dept_file + '.html', 'w')  # 파일 오픈
        fi.write((str)(html_base))
        fi.close()
