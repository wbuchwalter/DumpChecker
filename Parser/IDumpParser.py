import re
from DBAccess import DBAccess
from abc import ABCMeta, abstractmethod


class IDumpParser(object):
    __metaclass__ = ABCMeta

    def __init__(self, url):
        self.dump_id = ''
        self.dump_url = url
        self.dbAccess = DBAccess()

    def parse(self, withSaving=False):
        if withSaving:
            self.saveDump()
        return self.extractInfosFromDump(withSaving)


    def extractInfosFromDump(self,withSaving):
        rawDump = self.getRawDump()

        regexExprs = [r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b",
                      r"\n[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\n"]
        aggregatedMatches = []

        for expr in regexExprs:
            p = re.compile(expr)
            matches = p.findall(repr(rawDump))
            aggregatedMatches.extend(matches)

        if withSaving:
            self.saveMails(aggregatedMatches)
        return aggregatedMatches

    @abstractmethod
    def getRawDump(self):
        pass

    def saveMails(self, mails):
        for mail in mails:
            self.saveMail(mail)

    def saveMail(self, mail):
        dumpItem = {'mail': mail, 'dump_id': self.dump_id}
        self.dbAccess.insertDumpItem(dumpItem)

    def saveDump(self):
        self.dump_id = self.dbAccess.insertDump(self.dump_url)


    def getDumpUrl(self):
        return self.dump_url