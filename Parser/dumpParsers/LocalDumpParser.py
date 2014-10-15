from dumpParsers.IDumpParser import IDumpParser


class LocalDumpParser(IDumpParser):

    def __init__(self):
        IDumpParser.__init__(self)
        self.filePath = ''

    def parse(self, filePath, withSaving=True):
          self.filePath = filePath
          fi = open(filePath)
          url = fi.readline().rstrip()
          IDumpParser.parse(self, url, withSaving)

    def getRawDump(self):
        fi = open(self.filePath)
        raw = fi.read()
        return raw
