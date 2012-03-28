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

connector = sqlite3.connect("/tmp/test.db");
cursor = connector.cursor();

if (os.environ["REQUEST_METHOD"] == "POST"):
    form = cgi.FieldStorage();
    id = form["id"].value;
    ip = os.environ["REMOTE_ADDR"];
    cursor.execute("SELECT COUNT(id) FROM not_cute");
    new_id = cursor.fetchone()[0];
    connector.execute("INSERT INTO not_cute VALUE (%s, '%s', %s)" % (new_id, ip, id));
    connector.commit();
    print("OK");
else:
    print "Error";
