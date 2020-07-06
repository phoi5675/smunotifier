# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import date

class NotiFinder:
    def __init__(self, notiListWrapperClassKeyword, notiLineWrapperElementKeyword,
                 titleClassKeyword, dateClassKeyword, hrefElementKeyword):
        self.notiListWrapperClassKeyword = notiListWrapperClassKeyword
        self.notiLineWrapperElementKeyword = notiLineWrapperElementKeyword
        self.titleClassKeyword = titleClassKeyword
        self.dateClassKeyword = dateClassKeyword
        self.hrefElementKeyword = hrefElementKeyword
        
    def findAllWrappedNotiLine(self, scrapedHtml):
        return scrapedHtml.find(class_=self.notiListWrapperClassKeyword).find_all(self.notiLineWrapperElementKeyword)

    def findTitleInString(self, wrappedNotiLine):
        foundTitleTag = wrappedNotiLine.find(class_=self.titleClassKeyword)

        resultTitle = foundTitleTag.get_text()
        return resultTitle

    def findDateInString(self, wrappedNotiLine):
        foundDateTag = wrappedNotiLine.find(class_=self.dateClassKeyword)
        foundDateTag.span.clear()

        resultDate = foundDateTag.get_text()
        return resultDate

    def findHrefInString(self, wrappedNotiLine, webLinkForScrap):
        foundHrefTag = wrappedNotiLine.find(self.hrefElementKeyword)
        resultHref = webLinkForScrap + wrappedNotiLine.a.get('href')

        return resultHref

    @staticmethod
    def isToday(scrapDate):
        today = date.today().isoformat()
        if scrapDate == today:
            return True
        else:
            return False

    @staticmethod
    def webToLxmlClass(webPage):
        def removeBlank(html):
            html = html.replace("\t", "")
            html = html.replace("\n", "")
            html = html.replace("\r", "")

            return html

        requestedHtml = requests.get(webPage)
        textHtml = requestedHtml.text

        textHtml = removeBlank(textHtml)

        return BeautifulSoup(textHtml, 'lxml')

