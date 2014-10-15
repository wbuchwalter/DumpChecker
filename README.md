DumpChecker
===========

A tool to check if an email adresse has been compromised.

DumpChecker is divided into two modules:
  * Parser
  * API


Parser
------
A set of python classes that parse tweets from @dumpmon to detect new dumps.
New dumps are then downloaded and saved into the DB.


API
------
A node.js application, that allow anyone to check if his email address has been compromised.



@dumpmon: http://raidersec.blogspot.ca/2013/03/introducing-dumpmon-twitter-bot-that.html#more
