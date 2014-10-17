import datetime
from pymongo import MongoClient
from pymongo.errors import BulkWriteError


class DatabaseController:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.leakChecker
        self.dumpItems = self.db.dumpItems

    def insertDump(self, dumpUrl):
        dumps = self.db.dumps
        dump = {"url": dumpUrl,
                "date": datetime.datetime.utcnow()}
        dump_id = dumps.insert(dump)
        return dump_id

    def getDumpsUrls(self):
        dumps = self.db.dumps.find()
        dumpsUrls = []
        for dump in dumps:
            dumpsUrls.append(dump['url'])
        return dumpsUrls

    def insertDumpItem(self, dumpItem):
        di_id = self.dumpItems.insert(dumpItem)
        return di_id

    def dumpExists(self, dumpUrl):
        return self.db.dumps.find({'url': dumpUrl}).count() > 0

    def insertBulkDumpItems(self, dumpItems):
        bulk = self.dumpItems.initialize_unordered_bulk_op()
        for dumpItem in dumpItems:
            bulk.insert(dumpItem)
        try:
            bulk.execute()
        except BulkWriteError as bwe:
            print(bwe.details)



