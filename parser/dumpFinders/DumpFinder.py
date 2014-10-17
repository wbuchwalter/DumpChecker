__author__ = 'Will'
from DatabaseController import DatabaseController
from abc import abstractmethod

class DumpFinder(object):

    def __init__(self, url):
        self.url = url
        self.dbAccess = DatabaseController()

    def checkIfAlreadyProcessed(self,url):
        return self.dbAccess.dumpExists(url)

    def getOldDumpsUrls(self):
        return self.dbAccess.getDumpsUrls()

    @abstractmethod
    def getNewDumpsUrls(self):
        raise NotImplementedError()