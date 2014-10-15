from dumpParsers.IDumpParser import IDumpParser

__author__ = 'Will'
'''
Grab the data from the url, save it to the disk so we don't have to download it again if we want to reparse everything, and parse the data
'''

import urllib
from DumpSaver import DumpSaver

class NetDumpParser(IDumpParser):

    def __init__(self):
        IDumpParser.__init__(self)

    def getRawDump(self):
        i = urllib.urlopen(self.dump_url)
        html = i.read()
        self.saveRawDump(html)
        return html

    def saveRawDump(self, rawData):
        dumpSaver = DumpSaver()
        dumpSaver.writeDumpToFile(rawData, self.dump_url)
