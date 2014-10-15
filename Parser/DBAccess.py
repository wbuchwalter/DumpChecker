import datetime
from pymongo import MongoClient

class DBAccess:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.leakChecker

    def insertDump(self, dumpUrl):
        dumps = self.db.dumps
        dump = {"url": dumpUrl,
                "date": datetime.datetime.utcnow()}
        dump_id = dumps.insert(dump)
        return dump_id

    def getOldDumpsUrls(self):
        dumps = self.db.dumps.find()
        dumpsUrls = []
        for dump in dumps:
            dumpsUrls.append(dump['url'])
        return dumpsUrls

    def insertDumpItem(self, dumpItem):
        dumpItems = self.db.dumpItems
        di_id = dumpItems.insert(dumpItem)
        return di_id

    def dumpExists(self, dumpUrl):
        return self.db.dumps.find({'url': dumpUrl}).count() > 0
