import DumpFinder
from NetDumpParser import NetDumpParser
from time import sleep

dumpFinder = DumpFinder.DumpFinder("https://twitter.com/dumpmon")
newDumpsUrls = dumpFinder.getNewDumpsUrls()
print(repr(len(newDumpsUrls)) + ' new dumps.\n')
for dumpUrl in newDumpsUrls:
    print(dumpUrl + '\n')
    '''to avoid pastebin ban'''
    sleep(5)
    dumpParser = NetDumpParser(dumpUrl)
    print(dumpParser.parse(True))





