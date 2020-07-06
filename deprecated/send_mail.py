#-*- coding:utf-8 -*-
# 구글 스프레드시트 import
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# 이메일 import
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import const
# Beautifulsoup
from bs4 import BeautifulSoup

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
# 이메일 유효성 검사 함수
def is_valid(addr):
    import re
    if re.match('(^[a-zA-Z-0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr):
        return True
    else:
        return False

# 이메일 보내기 함수
def send_mail(smtp, addr, subj_layout, cont_layout, attachment=None):
    if not is_valid(addr):
        print("Wrong email: " + addr)
        return

    # 텍스트 파일
    msg = MIMEMultipart("alternative")
    # 첨부파일이 있는 경우 mixed로 multipart 생성
    if attachment:
        msg = MIMEMultipart('mixed')
    msg["From"] = SMTP_USER
    msg["To"] = addr
    msg["Subject"] = subj_layout
    # list 를 str 로 변환
    contents = ''
    for cont_line in cont_layout:
        contents = contents + cont_line
    text = MIMEText(contents, 'html', _charset='utf-8')
    msg.attach(text)
    # 첨부파일이 있으면
    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders
        file_data = MIMEBase("application", "octect-stream")
        file_data.set_payload(open(attachment, "rb").read())
        encoders.encode_base64(file_data)
        import os
        filename = os.path.basename(attachment)
        file_data.add_header("Content-Disposition", 'attachment', filename=('UTF-8', '', filename))
        msg.attach(file_data)

    # 메일 발송
    smtp.sendmail(SMTP_USER, addr, msg.as_string())


'''
메일 관련 설정
'''
# SMTP 접속을 위한 서버, 계정 설정
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
# 보내는 메일 계정
SMTP_USER = "userid@gmail.com"
SMTP_PASSWORD = "userpwd"

# smtp로 접속할 서버 정보를 가진 클래스변수 생성
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
# 해당 서버로 로그인
smtp.login(SMTP_USER, SMTP_PASSWORD)

'''
스크래핑한 html 파일을 읽고, 메일 발송
'''

str_list = {}
# 저장한 파일 불러오기
for dept_index in const.DEPFIARY:
    try:
        file = open(const.FILEPATH + 'html/' + dept_index + '.html', 'r')
        str_list[dept_index] = file.readlines()
        file.close()
    except:
        pass

'''
구글 스프레드시트 설정
'''
json_file_name = const.FILEPATH + 'smunoti-0ef6246c514e.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1dho7cyxKFNDHpMZYY9C5u4kSJIfoOIGWo8GiFi4bHEY/edit#gid=313462459'
# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)
# 시트 선택하기
worksheet = doc.worksheet('설문지 응답 시트1')

cell_data = worksheet.acell('B2').value
i = 2 # 셀의 데이터는 2행부터 시작
while worksheet.acell('A' + (str)(i)).value != '':
    # 구독 취소 한 사람의 경우 루프 넘김
    if worksheet.acell('d' + (str)(i)).value == 'O':
        continue
    addr = worksheet.acell('b' + (str)(i)).value # 메일 주소
    maj = worksheet.acell('c' + (str)(i)).value # 전공 분류
    index = const.DEPDICTARY[maj]

    # 파일로부터 읽은 str 이 존재하는 경우에만 메일 발송
    try:
        if str_list[index] != '':
            # 메일 발송
            send_mail(smtp, addr, "상명대학교 공지사항", str_list[index])
    except:
        pass
    i += 1


# 닫기
smtp.close()
