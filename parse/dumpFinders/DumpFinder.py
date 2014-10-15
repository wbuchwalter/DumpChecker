__author__ = 'Will'
from DBAccess import DBAccess
from abc import abstractmethod

class DumpFinder(object):

    def __init__(self, url):
        self.url = url
        self.dbAccess = DBAccess()

    def checkIfAlreadyProcessed(self,url):
        return self.dbAccess.dumpExists(url)

    def getOldDumpsUrls(self):
        return self.dbAccess.getOldDumpsUrls()

    @abstractmethod
    def getNewDumpsUrls(self):
        raise NotImplementedError()