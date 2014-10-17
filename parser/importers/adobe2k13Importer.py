__author__ = 'Will'

from DatabaseController import DatabaseController
import time
import threading

class parsingMonitor(object):

    TOTAL_LINES = 152989508
    counter = 0

    @classmethod
    def updateCounter(cls, nb):
        cls.counter += nb

    @classmethod
    def startMonitoring(cls):
        cls.printStatus()


    @classmethod
    def printStatus(cls):
        sleeptime = 1
        while 1:
            oldCount = cls.counter
            time.sleep(sleeptime)
            speed = (cls.counter - oldCount)/sleeptime
            perct = cls.getPercentageDone()
            print(repr(perct) + '%   @' + repr(speed) + '/s\n')


    @classmethod
    def getPercentageDone(cls):
        return (cls.counter/cls.TOTAL_LINES)*100

class adobe2k13ImporterThread(threading.Thread):

    def __init__(self, threadid, filepath, sliceStart, sliceEnd):
        threading.Thread.__init__(self)
        self.sliceStart = sliceStart
        self.sliceEnd = sliceEnd
        self.threadid = threadid
        self.itemsToInsert = []
        self.dbCtrl = DatabaseController()
        self.dump_id = self.dbCtrl.insertDump('Adobe 2013 Mega dump')
        self.lineCounter = 0
        try:
            self.file = open(filepath, 'r')
        except IOError, e:
            print('opening failed: ' + e)

    def run(self):
        print('starting a new parsing thread\n')
        if self.sliceStart > 0:
            print('thread ' + repr(self.threadid) + ' fast skipping to sliceStart\n')
        self.parse()
        print('Parsing thread exiting')

    def parse(self):
        for line in self.file:
            self.lineCounter += 1
            if self.sliceStart >= self.lineCounter:
                continue
            if self.lineCounter <= self.sliceEnd:
                self.parseLine(line)
                parsingMonitor.updateCounter(1)
            else:
                break

    def parseLine(self, line):
        if len(line) < 10:
            return
        cleanLine = line.rstrip('|--\n')
        columns = cleanLine.split('-|-')
        self.saveRow(columns)

    def saveRow(self, arr):
        arrLen = len(arr)
        if arrLen < 3:
            return
        dumpItem = {
            'mail': arr[2],
            'pwd': arr[3] if arrLen > 3 else '',
            'secret': arr[4] if arrLen > 4 else '',
            'dump_id': self.dump_id
        }
        self.itemsToInsert.append(dumpItem)
        if len(self.itemsToInsert) % 500 == 0:
            self.dbCtrl.insertBulkDumpItems(self.itemsToInsert)
            self.itemsToInsert = []



parserThread = adobe2k13ImporterThread(1, '../dumps/cred', 0, 3000000)
parserThread2 = adobe2k13ImporterThread(2, '../dumps/cred', 3000001, 6000000)
parserThread3 = adobe2k13ImporterThread(3, '../dumps/cred', 6000001, 10000000)

parserThread.start()
parserThread2.start()
# parserThread3.start()

parsingMonitor.startMonitoring()
