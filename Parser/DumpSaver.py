__author__ = 'Will'
import time

class DumpSaver(object):

    def __init__(self):
        pass

    def writeDumpToFile(self, rawData, originalUrl):
        wf = open('dumps/' + time.strftime("%Y%m%d-%H%M%S") + '.txt', 'w')
        finalData = originalUrl + '\n' + rawData
        wf.write(finalData.encode('utf-8'))