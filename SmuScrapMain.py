# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import const
import copy
from ExtractedNoti import *
from NotiFinder import NotiFinder


def webScrap(notiFinder, notiListAll, webPageList, link=''):
    for notiList, webPage in zip(notiListAll, webPageList):
        scrapedHtml = NotiFinder.webToLxmlClass(webPage)
        notiLines = notiFinder.findAllWrappedNotiLine(scrapedHtml)

        # 학교 홈페이지 공지와 학과 공지 배열이 다르므로 try except 문으로 해결
        try:
            notiList.category = const.GENWEBDICT[webPage]
        except KeyError:
            notiList.category = const.DEPWEBDICT[webPage]

        for notiLine in notiLines:
            date = notiFinder.findDateInString(notiLine)
            '''
            # 스크랩 잘 되는지 테스트 하는 부분 시작
            title = notiFinder.findTitleInString(notiLine)
            if link == '':
                href = notiFinder.findHrefInString(notiLine, webPage)
            else:
                href = notiFinder.findHrefInString(notiLine, link)

            notiList.extractedNotiList.append(ExtractedNoti(title, date, href))
            notiList.numOfNoti = notiList.numOfNoti + 1
            # 스크랩 잘 되는지 테스트 하는 부분 끝
            '''
            if NotiFinder.isToday(date):  # 오늘 날짜와 일치하는 공지만 추가
                title = notiFinder.findTitleInString(notiLine)
                # 학교 공지와 학교 공지 방식이 다르므로 조건문으로 나눔
                if link == '':
                    href = notiFinder.findHrefInString(notiLine, webPage)
                else:
                    href = notiFinder.findHrefInString(notiLine, link)

                notiList.extractedNotiList.append(ExtractedNoti(title, date, href))
                notiList.numOfNoti = notiList.numOfNoti + 1
            else:
                continue


def setTagAttribute(value, attribute, htmlTag):
    # 기존에 attr 에 value 가 있으면 기존값을 덮어씌우는 경우가 있으므로
    try:
        htmlTag[attribute] = htmlTag[attribute] + value + ";"
    except KeyError:
        htmlTag[attribute] = value + ";"


def addCategoryNotiToHtml(notiList, htmlBase):
    def addHrTag(htmlTag):
        hrTag = BeautifulSoup("<hr>", "lxml")
        htmlTag.insert_after(hrTag.hr)

    def addCategoryToHtmlListTag(category, htmlBase):
        headerTag = htmlBase.new_tag("h1")
        headerTag.string = category + " 공지사항"

        listTag = htmlBase.new_tag("ul")
        listTag['class'] = category

        setTagAttribute("font-size:22px", "style", headerTag)

        setTagAttribute("font-size:15px", "style", listTag)
        setTagAttribute("padding-left:15px", "style", listTag)  # li 태그의 들여쓰기 없애기

        htmlBase.body.append(headerTag)
        htmlBase.body.append(listTag)

    def addNotiLineToHtmlInUnorderedListTag(notiList, htmlBase):
        # notiList 는 학사, 취업 등 한 섹션의 공지를 담은 리스트
        categoryDivTag = htmlBase.find("ul", class_=notiList.category)
        for i in range(notiList.numOfNoti):
            unorderedListTag = htmlBase.new_tag("li")

            notiTag = htmlBase.new_tag("a", href=notiList.extractedNotiList[i].href)
            notiTag.string = notiList.extractedNotiList[i].title

            unorderedListTag.append(notiTag)

            addHrTag(categoryDivTag)

            categoryDivTag.append(unorderedListTag)

    def hasNoti(notiList):
        if notiList.numOfNoti != 0:
            return True
        else:
            return False

    if hasNoti(notiList):
        addCategoryToHtmlListTag(notiList.category, htmlBase)
        addNotiLineToHtmlInUnorderedListTag(notiList, htmlBase)
    else:
        pass


def addInfoTag(html):
    infoTagSoup = BeautifulSoup(const.INFOTAG, 'lxml')
    infoTag = infoTagSoup.p

    setTagAttribute("font-size:13px", "style", infoTag)

    html.body.append(infoTag)


def htmlToFile(html, filename):
    # 메인 파이썬이 있는 폴더 내의 html 폴더에 저장
    # html 폴더가 없는 경우, 오류 발생
    file = open(const.FILEPATH + 'html/' + filename + '.html', 'w')
    file.write(str(html))

    file.close()


if __name__ == '__main__':
    genNotiListAll = list(ExtractedNotiList() for i in range(const.GENINT))
    deptNotiListAll = list(ExtractedNotiList() for i in range(const.DEPINT))

    notiFinder = NotiFinder('board-thumb-wrap', 'dl', 'board-thumb-content-title', 'board-thumb-content-date', 'a')

    # 일반 공지 스크랩
    webScrap(notiFinder, genNotiListAll, const.GENWEB, const.GENERALNOTILINK)

    # 학과 공지 스크랩
    webScrap(notiFinder, deptNotiListAll, const.DEPWEB)

    # 받은 공지를 html 로 넘기기
    htmlBaseInString = const.HTMLBASE
    htmlBase = BeautifulSoup(htmlBaseInString, 'lxml')

    # 학교 일반 공지 전체 추가
    for singleCategoryNotiList in genNotiListAll:
        addCategoryNotiToHtml(singleCategoryNotiList, htmlBase)

    # 학과 공지
    for singleCategoryNotiList, filename in zip(deptNotiListAll, const.DEPFIARY):
        # 1. copy 를 이용하여 일반 공지를 담은 htmlBase 를 유지한 채 htmlToSaveDeptNoti 에 htmlBase 내용 복사
        #    n 번째 루프에서는 덮어쓰기
        htmlToSaveDeptNoti = copy.copy(htmlBase)

        # 2. 한 학과의 공지를 htmlToSaveDeptNoti 에 저장
        addCategoryNotiToHtml(singleCategoryNotiList, htmlToSaveDeptNoti)

        # 3. INFOTAG 추가
        addInfoTag(htmlToSaveDeptNoti)

        # 4. htmlBase 를 학과 파일로 저장
        htmlToFile(htmlToSaveDeptNoti, filename)
