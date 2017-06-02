#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re
import io
from subprocess import Popen, PIPE




if os.path.exists('../CHANGELOG.md'):
    os.remove('../CHANGELOG.md')


if not os.path.exists('../CHANGELOG.md'):
    open('../CHANGELOG.md', 'w').close()


def deleteContent (file):
	file.seek(0)
	file.truncate()

with open('../CHANGELOG.md','r') as f:
	f.seek(0)
	first_char = f.read(1)
	if not first_char: 
		previous_date = str("[' 2017-05-20 17:47:16 ']")
	else:
		date = re.findall(r'\d{4}-\d{2}-\d{2}.\d{2}.\d{2}.\d{2}', f.readline())

		converted_date = datetime.datetime.strptime(" ".join(date), '%Y-%m-%d %H:%M:%S')
		seconds_date = converted_date + datetime.timedelta(0,3)

		previous_date = str("[' " + str(seconds_date) + " ']")

f = open('../CHANGELOG.md','r')
changelog_old = f.readlines()

f.close()

f = open('../CHANGELOG.md','a')
deleteContent(f)

# Pull requests mal formateadas
#feature/MON-136  [UPDATE]: crear pipeline para los logs de mesos https://datiobd.atlassian.net/browse/MON-136



message = Popen("git log --since={pdate}  --pretty=format:'%b' --grep='Merge pull request'   --date=format:'%Y-%m-%d %H:%M:%S'".format(pdate=previous_date), shell= True, stdout=PIPE).stdout.read()
f.write(message + '\n')

for line in changelog_old:
	f.write(line)

f.close()
