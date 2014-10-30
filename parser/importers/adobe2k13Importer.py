__author__ = 'Will'

from DatabaseController import DatabaseController
import time
import threading
import sys

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
        sleeptime = 2
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
            'secret': arr[4] if arrLen > 4 else '',
            'dump_id': self.dump_id
        }
        self.itemsToInsert.append(dumpItem)
        if len(self.itemsToInsert) % 500 == 0:
            self.dbCtrl.insertBulkDumpItems(self.itemsToInsert)
            self.itemsToInsert = []


filePath = sys.argv[1]

parserThread = adobe2k13ImporterThread(1, filePath, 0, 75000000)
parserThread2 = adobe2k13ImporterThread(2, filePath, 75000001, 153000000)
parserThread.start()
parserThread2.start()

parsingMonitor.startMonitoring()
