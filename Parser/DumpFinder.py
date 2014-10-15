import urllib
from bs4 import BeautifulSoup
from DBAccess import DBAccess

class DumpFinder:

  def __init__(self, url):
    self.url = url
    self.dbAccess = DBAccess()

  def extractUrlsFromTwitterTimeline(self):
    timeline = urllib.urlopen(self.url)
    soup = BeautifulSoup(timeline)
    tweetLinks = soup.find_all('a', class_="twitter-timeline-link")
    dumpUrls = []
    for link in tweetLinks:
        dumpUrls.append(link.get('data-expanded-url'))
    return dumpUrls

  def getNewDumpsUrls(self):
    oldDumps = self.getOldDumpsUrls()
    timelineDumps = self.extractUrlsFromTwitterTimeline()
    newDumps = list(set(timelineDumps) - set(oldDumps))
    return newDumps

  def getOldDumpsUrls(self):
      return self.dbAccess.getOldDumpsUrls()

  def checkIfAlreadyProcessed(self,url):
      return self.dbAccess.dumpExists(url)


