DumpChecker
===========

A tool to allow anyone to check if their email has been compromised.

DumpChecker is divided into two parts:
  * Parser
  * Site


Parser
------
Python
A set of python classes that parse tweets from @dumpmon to detect new dumps.
New dumps are then downloaded and saved into the DB.
There are also some custom importers, to import very large dumps (Adobe 2013 for example) or to bypass pastebin API usage limitation.
Of course, no dump is included in the source.

API
------
A Node.js + Angular app.
Express, Stylus, Jade.


External Resources
------

@dumpmon: https://twitter.com/dumpmon

