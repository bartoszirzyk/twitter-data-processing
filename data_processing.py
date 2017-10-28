
# encoding=utf8
import csv
import json
from urllib.parse import urlparse
from urllib.parse import urlsplit

def transformTweet(tweet):
  tweet['urls_transformed'] = [transformURL(x) for x in json.loads(tweet['urls'])]
  return tweet


def transformURL(url):
  out = {'url': '', 'domain': ''}
  if 'expanded_url' in url.keys():
    r = urlsplit(url['expanded_url'])
    out['url'] = r.netloc + r.path
  out['domain'] = r.netloc
  return out


with open('InputData/tweets2.csv', 'r', encoding="utf-8") as inputfile:
  reader = csv.DictReader(inputfile)
  with open('OutputData/out.csv', 'w') as outputfile:
    foo = reader.fieldnames
    foo.append('urls_transformed')
    writer = csv.DictWriter(outputfile, fieldnames=foo)
    writer.writeheader()
    for row in reader:
      writer.writerow(transformTweet(row))
