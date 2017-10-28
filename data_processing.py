
# encoding=utf8
import re
import csv
import json


def transformTweet(tweet):
  tweet['urls'] = [transformURL(x) for x in json.loads(tweet['urls'])]
  return tweet

def transformURL(url):
  if 'expanded_url' in url.keys():
    return re.match('https?://[^\s\?\#]+', url['expanded_url']).group(0)

with open('InputData/tweets2.csv', 'r', encoding="utf-8") as inputfile:
  reader = csv.DictReader(inputfile)
  with open('OutputData/out.csv', 'w') as outputfile:
    writer = csv.DictWriter(outputfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in reader:
      writer.writerow(transformTweet(row))
