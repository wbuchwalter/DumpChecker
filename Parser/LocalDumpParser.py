from IDumpParser import IDumpParser


class LocalDumpParser(IDumpParser):

    def __init__(self, filePath):
        self.filePath = filePath
        fi = open(filePath)
        url = fi.readline().rstrip()
        IDumpParser.__init__(self, url)

    def getRawDump(self):
        fi = open(self.filePath)
        raw = fi.read()
        return raw
