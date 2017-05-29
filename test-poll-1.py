#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This test loads poll results.
#

import json
import requests
import datetime

quiet = False

r = requests.get('https://elections.huffingtonpost.com/pollster/api/v2/polls/gallup-27729')

if 200 == r.status_code:
    if 'application/json' in r.headers['content-type']:
        # print r.json()
        data = r.json()
    else:
        print "not json"
else:
    print "not 200"

# print r.text

text_a = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][0]["text"]
value_a = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][0]["value"]

if not quiet:
    print text_a
    print value_a

text_d = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][1]["text"]
value_d = data["poll_questions"][0]["sample_subpopulations"][0]["responses"][1]["value"]

if not quiet:
    print text_d
    print value_d

inJSON = json.dumps({text_a: value_a, text_d: value_d}, 
    sort_keys=True, 
    indent=4, 
    separators=(',', ' : '))

fileName = 'poll.json'
file = open(fileName, "w")
file.write(inJSON)
file.close()

today = datetime.datetime.now()
fileName = 'poll' + "." + str(today.month) + "." + str(today.day) + "." + str(today.year) + ".json"
file = open(fileName, "w")
file.write(inJSON)
file.close()
