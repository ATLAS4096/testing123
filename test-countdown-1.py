#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This test implements a date count up/down timer.
#

import json
import datetime

quiet = False

daysInOffice = datetime.datetime.now() - datetime.datetime(year=2017, month=1, day=20)
daysLeftInTerm = datetime.datetime(year=2021, month=1, day=20) - datetime.datetime.now()

if not quiet:
    print 'Days in office: ' + str(daysInOffice.days)
    print 'Days remaining in term: ' + str(daysLeftInTerm.days)

inJSON = json.dumps({'days_in_office': daysInOffice.days, 'days_remaining_in_term': daysLeftInTerm.days}, 
    sort_keys=True, 
    indent=4, 
    separators=(',', ' : '))

fileName = 'countdown.json'
file = open(fileName, "w")
file.write(inJSON)
file.close()


