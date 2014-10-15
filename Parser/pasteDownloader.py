'''
Not really part of the project:
Just a simple class that read leakUrls.txt, and copy the content of the url into a textfile
it takes to argument to start this. SliceStart and SliceEnd, the purpose of that, is to allow to simultaneously
parse the file from different servers: e.g: server1 process lines 0 - 1000 of the file, server2 1000 - 2000 etc..
This is useful because we have to sleep(5) between each url to prevent pastebin from blocking us.
'''



from time import sleep
import urllib
import datetime
import sys


def getData(url):
    raw = urllib.urlopen(url)
    html = raw.read()
    return html


fi = open('leakUrls.txt')
lines = fi.readlines()
sliceStart = int(sys.argv[1])
sliceEnd = int(sys.argv[2])
slicedLines = lines[sliceStart:sliceEnd]
i = sliceStart
startDate = datetime.datetime.now()
for dumpUrl in slicedLines:
    sleep(5)
    originalUrl = dumpUrl.rstrip('\n')
    if dumpUrl.find('pastebin') != -1:
        dumpUrl = originalUrl + '&paste_key=a03d8090fb48c45a9941c59d4c654859'
    i += 1
    stepDate = datetime.datetime.now()
    deltaTime = stepDate - startDate
    print('--- running since ' + str(deltaTime) + '\n --- parsing '+repr(i)+' :' + dumpUrl + '\n')
    rawData = getData(dumpUrl)
    wf = open('dumpFiles/' + repr(i) + '.txt', 'w')
    finalData = originalUrl+ '\n' + rawData
    wf.write(finalData)

