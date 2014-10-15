import glob
from LocalDumpParser import LocalDumpParser
from DumpFinder import DumpFinder
import sys

filesPath = glob.glob('./dumps/*.txt')
dumpFinder = DumpFinder('')
sliceStart = 0
sliceEnd = 0
try:
    sliceStart = int(sys.argv[1])
except IndexError:
    sliceStart = 0
try:
    sliceEnd = int(sys.argv[2])
except IndexError:
    sliceEnd = sliceStart+1000

i = 0
for filePath in filesPath[sliceStart:sliceEnd]:
    i += 1
    if i % 20 == 0:
        ''' clear terminal'''
        print chr(27) + "[2J"
        print('Processing dump ' + repr(i) + '\n')

    dumpParser = LocalDumpParser(filePath)
    if not dumpFinder.checkIfAlreadyProcessed(dumpParser.getDumpUrl()):
        dumpParser.parse(True)

