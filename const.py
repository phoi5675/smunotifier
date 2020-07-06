# 학교 공지
GENERALNOTILINK = "https://www.smu.ac.kr/lounge/notice/notice.do"  # 전체공지 / 스크랩된 href 와 결합 시 사용

ACADEMIC = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=19"  # 학사
GENERAL = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=20"  # 일반
VOLUNTEER = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=21"  # 사회봉사
SCHOLARSHIP = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=22"  # 장학
STUDENTLIFE = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=189"  # 학생생활
EMPLOYMENT = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=23"  # 채용
GLOBAL = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=190"  # 글로벌
SMARTATTEND = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=28"  # 스마트출결
CAREER = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=162"  # 진로취업
SAMMULSYS = "https://www.smu.ac.kr/lounge/notice/notice.do?mode=list&srCategoryId1=200"  # 샘물시스템

# 학과 공지
KJC = "https://www.smu.ac.kr/kjc/community/notice.do"  # 한콘
BIZ = "https://www.smu.ac.kr/smubiz/community/notice.do"  # 경영
ECO = "https://www.smu.ac.kr/economic/community/notice.do"  # 경제금융
NEW = "https://www.smu.ac.kr/newmajoritb/board/notice.do"  # 글로벌경영
COM = "https://www.smu.ac.kr/cm/community/notice.do"  # 융합경영
HI = "https://www.smu.ac.kr/hi/community/notice.do"  # 휴먼지능정보공
GAME = "https://www.smu.ac.kr/game01/community/notice.do"  # 게임
CS = "https://www.smu.ac.kr/cs/community/notice.do"  # 컴퓨터과학
ANI = "https://www.smu.ac.kr/animation/community/notice.do"  # 애니
ELEC = "https://www.smu.ac.kr/electric/community/notice.do"  # 전기공
ELOC = "https://www.smu.ac.kr/electronic/community/notice.do"  # 융합전자공
BIO = "https://www.smu.ac.kr/biotechnology/community/notice.do"  # 생명공
CEE = "https://www.smu.ac.kr/cee/community/notice.do"  # 화학에너지공
ICH = "https://www.smu.ac.kr/ichemistry/community/notice.do"  # 화공신소재
FOOD = "https://www.smu.ac.kr/foodnutrition/community/notice.do"  # 식품영양
CLOT = "https://www.smu.ac.kr/clothing2/community/notice.do"  # 의류
SMPE = "https://www.smu.ac.kr/smpe/community/notice.do"  # 스포츠건강
DAN = "https://www.smu.ac.kr/dance/undergraduate/undergraduate_notice.do"  # 무용예술
FINE = "https://www.smu.ac.kr/finearts/community/notice.do"  # 조형예술
LAD = "https://www.smu.ac.kr/smulad/community/notice.do"  # 생활예술
MUS = "https://www.smu.ac.kr/music/community/notice.do"  # 음악
HIS = "https://www.smu.ac.kr/history/community/notice.do"  # 역사콘텐츠
CC = "https://www.smu.ac.kr/cc/community/notice.do"  # 지적재산권
LIB = "https://www.smu.ac.kr/libinfo/community/notice.do"  # 문헌정보
SPA = "https://www.smu.ac.kr/space/community/notice.do"  # 공간환경
PUB = "https://www.smu.ac.kr/public/community/notice.do"  # 공공인재
FAM = "https://www.smu.ac.kr/smfamily/community/notice.do"  # 가족복지
SDMS = "https://www.smu.ac.kr/sdms/community/notice.do"  # 국가안보
KOED = "https://www.smu.ac.kr/koredu/community/notice.do"  # 국어교육
ENED = "https://www.smu.ac.kr/engedu/community/notice.do"  # 영어교육
PEDA = "https://www.smu.ac.kr/peda/community/notice.do"  # 교육
MAED = "https://www.smu.ac.kr/mathedu/community/notice.do"  # 수학교육

# 학교 전체 공지 링크 리스트
GENWEB = [ACADEMIC, GENERAL, VOLUNTEER, SCHOLARSHIP,
          STUDENTLIFE, EMPLOYMENT, GLOBAL, SMARTATTEND, CAREER, SAMMULSYS]

# 학과 공지 링크 리스트
DEPWEB = [KJC, BIZ, ECO, NEW, COM, HI, GAME, CS, ANI, ELEC, ELOC, BIO, CEE, ICH, FOOD, CLOT,
          SMPE, DAN, FINE, LAD, MUS, HIS, CC, LIB, SPA, PUB, FAM, SDMS, KOED, ENED, PEDA, MAED]

# 학교 전체 공지 배열 크기
GENINT = len(GENWEB)

# 학과 공지 배열 크기
DEPINT = len(DEPWEB)

# 파일 저장용 배열
DEPFIARY = ['kjc', 'biz', 'eco', 'new', 'com', 'hi', 'game', 'cs', 'ani', 'elec', 'eloc',
            'bio', 'cee', 'ich', 'food', 'clot', 'smpe', 'dan', 'fine', 'lad', 'mus', 'his',
            'cc', 'lib', 'spa', 'pub', 'fam', 'sdms', 'koed', 'ened', 'peda', 'maed']

# 구글 스프레드시트 -> 파일 읽기
DEPDICT = {"한콘": "kjc", "경영": "biz", "경제금융": "eco", "글로벌경영": "new", "융합경영": "com", "휴면지능정보공": "hi",
           "게임": "game", "컴퓨터과학": "cs", "애니": "ani", "전기공": "elec", "융합전자공": "eloc", "생명공": "bio",
           "화학에너지공": "cee", "화공신소재": "ich", "식품영양": "food", "의류": "clot", "스포츠건강": "smpe", "무용예술": "dan",
           "조형예술": "fine", "생활예술": "lad", "음악": "mus", "역사콘텐츠": "his", "지적재산권": "cc", "문헌정보": "lib",
           "공간환경": "spa", "공공인재": "pub", "가족복지": "fam", "국가안보": "sdms", "국어교육": "koed", "영어교육": "ened",
           "교육": "peda", "수학교육": "maed"}

# -------------------- html -------------------- #
# 학교 전체 공지 딕셔너리
GENWEBDICT = {
    ACADEMIC: "학사", GENERAL: "일반", VOLUNTEER: "사회봉사", SCHOLARSHIP: "장학",
    STUDENTLIFE: "학생생활", EMPLOYMENT: "채용", GLOBAL: "글로벌", SMARTATTEND: "스마트출결",
    CAREER: "진로", SAMMULSYS: "샘물시스템"
}
# 학과 공지 딕셔너리
DEPWEBDICT = {
    KJC: "한일문화컨텐츠전공", BIZ: "경영학부", ECO: "경제금융학부", NEW: "글로벌경영학과", COM: "융합경영학과",
    HI: "휴먼지능정보공학전공", GAME: "게임전공", CS: "컴퓨터과학전공", ANI: "애니메이션전공", ELEC: "전기공학전공",
    ELOC: "융합전자공학전공", BIO: "생명공학전공", CEE: "화학에너지공학전공", ICH: "화공신소재전공", FOOD: "식품영양학전공",
    CLOT: "의류학전공", SMPE: "스포츠건강관리전공", DAN: "무용예술전공", FINE: "조형예술전공", LAD: "생활예술전공",
    MUS: "음악학부", HIS: "역사콘텐츠전공", CC: "지적재산권전공", LIB: "문헌정보학전공", SPA: "공간환경학부",
    PUB: "공공인재학부", FAM: "가족복지학과", SDMS: "국가안보학과", KOED: "국어교육과", ENED: "영어교육과",
    PEDA: "교육학과", MAED: "수학교육"
}

# HTML 파일 베이스
HTMLBASE = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset=\"utf-8\">
    </head>
    <body>
    </body>
</html>
'''

# HTML 아래에 구독 신청 / 취소 등 정보를 위한 p 태그 및 신청 / 취소 링크
SUBSCRIBELINK = "https://forms.gle/F2o6VgXpuUESyW4i7"
UNSUBSCRIBELINK = "https://forms.gle/55mSgQkuweBL8XbJ8"
MAILLINK = "phoismunotifier@gmail.com"
INFOTAG = '''
<p>
다른 학우분들도 메일을 받아 볼 수 있게 해주세요! 신청은 <a href=''' + SUBSCRIBELINK + '''>여기</a> 에서 할 수 있습니다<br>
구독을 중단하고 싶은 경우 <a href=''' + UNSUBSCRIBELINK + '''>여기</a>에 메일을 적어주세요<br>
기타 문의사항은 <a href=''' + MAILLINK + '''>''' + MAILLINK + '''</a>으로 문의 바랍니다
</p>
'''

# -------------------- 파일 -------------------- #
# 파일 경로 / 루트 폴더까지만 지정
FILEPATH = "/home/phoi/Documents/smu_scrap/"

# -------------------- email 발송 -------------------- #
# json 파일 이름
JSON = '.json'

# 이메일 ID / PW
SENDERID = "@gmail.com"
SENDERPWD = "pwd"

# 스프레드시트 링크
SPREADSHEETLINK = "https://docs.google.com/spreadsheets/"

# 시트 이름
SHEETNAME = "설문지 응답 시트1"

# email 제목
EMAILTITLE = "상명대학교 공지사항"

# -------------------- deprecated values -------------------- #
GENFIARY = ['gen']