from dumpFinders.TweetDumpFinder import TweetDumpFinder
from dumpParsers.NetDumpParser import NetDumpParser

__author__ = 'Will'

from time import sleep


class TweetScanner(object):

    def __init__(self,timelineUrl):
        self.timelineUrl = timelineUrl

    def scan(self):
        dumpFinder = TweetDumpFinder(self.timelineUrl)
        newDumpsUrls = dumpFinder.getNewDumpsUrls()
        print(repr(len(newDumpsUrls)) + ' new dumps.\n')
        dumpParser = NetDumpParser()
        for dumpUrl in newDumpsUrls:
            print(dumpUrl + '\n')
            '''to avoid pastebin ban'''
            sleep(5)
            print(repr(len(dumpParser.parse(dumpUrl,True))) + ' mails extracted \n')