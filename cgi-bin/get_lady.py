#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import cgi
import json
import sqlite3
import urllib
import cgitb

cgitb.enable();

form = cgi.FieldStorage();
try:
    start = form["start"].value();
    end = form["end"].value();
except KeyError:
    start = 0;
    end = 10;

connector = sqlite3.connect("/tmp/test.db");
cursor = connector.cursor();

cursor.execute("SELECT url, title, filename FROM ladys" );

result = {"stop": False, "results": [{"url": row[0], "title": row[1], "image": str("/img/" + row[2])} for row in cursor.fetchall()[start:end]]}

print json.dumps(result);

