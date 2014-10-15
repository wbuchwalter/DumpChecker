import urllib

from bs4 import BeautifulSoup

from dumpFinders.DumpFinder import DumpFinder


class TweetDumpFinder(DumpFinder):

    def __init__(self, url):
        DumpFinder.__init__(self, url)

    def getNewDumpsUrls(self):
        oldDumps = self.getOldDumpsUrls()
        timelineDumps = self.extractUrlsFromTwitterTimeline()
        newDumps = list(set(timelineDumps) - set(oldDumps))
        return newDumps

    def extractUrlsFromTwitterTimeline(self):
        timeline = urllib.urlopen(self.url)
        soup = BeautifulSoup(timeline)
        tweetLinks = soup.find_all('a', class_="twitter-timeline-link")
        dumpUrls = []
        for link in tweetLinks:
            dumpUrls.append(link.get('data-expanded-url'))
        return dumpUrls





