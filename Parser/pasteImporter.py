import glob
import sys
import threading
from dumpFinders.DumpFinder import DumpFinder
from dumpParsers.LocalDumpParser import LocalDumpParser

class parsedDumpCounter():
    counter = 0

    def __init__(self):
        pass

    @classmethod
    def updateCounter(cls, nbNewDumpParsed, emitingThreadID):
        cls.counter += nbNewDumpParsed
        print chr(27) + "[2J"
        print('Update from thread ' + repr(emitingThreadID) + '\n')
        print(repr(cls.counter))


class parsingThread(threading.Thread):

    def __init__(self, threadID, sliceStart, sliceEnd):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.sliceStart = sliceStart
        self.sliceEnd = sliceEnd
        self.dumpFinder = DumpFinder('')
        self.dumpParser = LocalDumpParser()

    def run(self):
        i = 0
        for filePath in filesPath[self.sliceStart:self.sliceEnd]:
            i += 1
            if i % 20 == 0:
                parsedDumpCounter.updateCounter(i,self.threadID)
                i = 0

            self.dumpParser.parse(filePath)
            if not self.dumpFinder.checkIfAlreadyProcessed(self.dumpParser.getDumpUrl()):
                self.dumpParser.parse(True)

        print('Thread ' + repr(self.threadID) + ' exiting')


filesPath = glob.glob('./dumps/*.txt')
_sliceStart = 0
_sliceEnd = 0
try:
    _sliceStart = int(sys.argv[1])
except IndexError:
    _sliceStart = 0
try:
    _sliceEnd = int(sys.argv[2])
except IndexError:
    _sliceEnd = _sliceStart+1000

nbToParse = _sliceEnd - _sliceStart
thread1 = parsingThread(1, _sliceStart, _sliceStart + nbToParse/4)
thread2 = parsingThread(2, _sliceStart + nbToParse/4+1, _sliceStart + nbToParse/2)
thread3 = parsingThread(3, _sliceStart + nbToParse/2+1, _sliceStart + (nbToParse/4)*3)
thread4 = parsingThread(4, _sliceStart + (nbToParse/4)*3+1, _sliceEnd)

thread1.start()
thread2.start()
thread3.start()
thread4.start()


