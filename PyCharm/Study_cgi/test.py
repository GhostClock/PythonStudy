#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

print "Content-type:text/html"
print
print '<head>'
print '<meta charset="utf-8">'
print '</head>'
print "<h1>环境变量</h1><br/>"
print "<ul>"
for key in os.environ.keys():
    print "<li><span style='color:green'>%30s</span> : %s </li>" % (key,os.environ[key])
print "</ul>"