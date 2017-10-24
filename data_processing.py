
# encoding=utf8  
import re
import urllib.request
import asyncio
import csv


def findRedirection(url):
  req = urllib.request.Request(url=url)
  resp = urllib.request.urlopen(req, timeout=10)
  return resp.geturl()


def filterURLs(tweet):
  return [findRedirection(x) for x in re.findall(r'(https?://[^\s]+)', tweet)]


with open('InputData/tweets.csv', 'r',encoding="utf-8") as inputfile:
  reader = csv.DictReader(inputfile)
  with open('OutputData/out.csv','w') as outputfile:
    fieldnames = ['twid', 'urls']
    writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
      writer.writerow({'twid': row['twid'], 'urls': filterURLs(row['tweet'])})