
# encoding=utf8
import re
import csv
import json


def transformURL(url):
  if any(url):
    return re.match('https?://[^\s\?\#]+', url['expanded_url']).group(0)

with open('InputData/tweets2.csv', 'r', encoding="utf-8") as inputfile:
  reader = csv.DictReader(inputfile)
  with open('OutputData/out.csv', 'w') as outputfile:
    fieldnames = ['twid', 'urls']
    writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
      writer.writerow({'twid': row['twid'], 'urls': [transformURL(x) for x in json.loads(row['urls'])]})
