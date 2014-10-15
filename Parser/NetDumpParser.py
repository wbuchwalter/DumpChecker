__author__ = 'Will'

from IDumpParser import IDumpParser
import urllib


class NetDumpParser(IDumpParser):

    def __init__(self, url):
        IDumpParser.__init__(self, url)

    def getRawDump(self):
        i = urllib.urlopen(self.dump_url)
        html = i.read()
        return html