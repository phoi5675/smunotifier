#-*- coding:utf-8 -*-
# 구글 스프레드시트 import
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# 이메일 import
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import const

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


# 이메일 발송 함수
def send_mail(smtp, addr, subj_layout, cont_layout, attachment=None):
    if not is_valid(addr):
        print("Wrong email: " + addr)
        return

    # 텍스트 파일
    msg = MIMEMultipart("alternative")
    # 첨부파일이 있는 경우 mixed로 multipart 생성
    if attachment:
        msg = MIMEMultipart('mixed')
    msg["From"] = smtp.user
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
    smtp.sendmail(smtp.user, addr, msg.as_string())


def connectSmtp():
    # SMTP 접속을 위한 서버, 계정 설정
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465
    # 보내는 메일 계정
    SMTP_USER = const.SENDERID
    SMTP_PASSWORD = const.SENDERPWD

    # smtp로 접속할 서버 정보를 가진 클래스변수 생성
    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    # 해당 서버로 로그인
    smtp.login(SMTP_USER, SMTP_PASSWORD)

    return smtp


def makeHtmlDictFromFile(htmlDict):
    for filename in const.DEPFIARY:
        try:
            file = open(const.FILEPATH + 'html/' + filename + '.html', 'r')
            htmlDict[filename] = file.readlines()
            file.close()
        except FileNotFoundError:
            pass


def getSpreadSheet():
    jsonFileName = const.FILEPATH + const.JSON
    credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonFileName, scope)
    gc = gspread.authorize(credentials)
    # 스프레스시트 문서 가져오기
    return gc.open_by_url(const.SPREADSHEETLINK)


def sendMailFromWorksheet(worksheet):
    i = 2  # 셀의 데이터는 2행부터 시작
    while worksheet.acell('A' + str(i)).value != '':
        # 구독 취소 한 사람의 경우 루프 넘김
        if worksheet.acell('d' + str(i)).value == 'O':
            continue
        mailAddr = worksheet.acell('b' + str(i)).value  # 메일 주소
        maj = worksheet.acell('c' + str(i)).value  # 전공 분류
        index = const.DEPDICT[maj]

        # 파일이 존재하는 학과만 공지 발송
        # 학교 공지가 없고, 학과 공지만 있을 때, 공지가 없는 학과가 생기는 경우
        # 파일을 읽지 못하고 htmlDict 에 html 과 key 값이 저장 되지 않아 KeyError 발생 가능
        try:
            if htmlDict[index] != '':
                # 메일 발송
                send_mail(smtp, mailAddr, const.EMAILTITLE, htmlDict[index])
        except KeyError:
            pass
        i += 1


if __name__ == '__main__':
    # SMTP 서버 연결
    smtp = connectSmtp()

    htmlDict = {}
    # html 파일 읽고 html 딕셔너리에 담기
    makeHtmlDictFromFile(htmlDict)

    # 구글 스프레드시트 불러오기
    doc = getSpreadSheet()

    # 시트 선택하기
    worksheet = doc.worksheet(const.SHEETNAME)

    # 스프레드시트 목록에서 메일 보내기
    sendMailFromWorksheet(worksheet)

    # 닫기
    smtp.close()
