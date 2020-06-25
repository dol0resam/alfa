# idea = ayman
__author__ = "sams3pi0l"
import urllib.request , urllib.error, urllib.parse
import requests
import json
import os
url = input("Url = ") # url http/https://example.com/test.php?=
dirs = json.loads(open('dirs.json').read())
for dir in dirs:
    url_extra = dir.lower()
    newurl = url + url_extra 
    response = urllib.request.urlopen(newurl)
    webContent = response.read()
    print("getting %s from %s and writing to gotit.txt" % (url_extra, newurl))

file = open('gotit.txt', 'wb')
file.write(webContent + "\n")
file.close
os.fileopen('gotit.txt')

exit()
