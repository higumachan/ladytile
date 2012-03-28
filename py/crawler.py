import urllib2
import json
import face
import os
import sqlite3
from urlparse import urlparse
from pit import Pit

INNER_SET = "206702"
BABY_DALL = "100448"
rakuten = Pit.get("rakuten");
DEV = rakuten["dev"];
AFI = rakuten["afi"];

connector = sqlite3.connect("/tmp/test.db");
cursor = connector.cursor();

for i in range(1, 101):
    s = urllib2.urlopen("http://api.rakuten.co.jp/rws/3.0/json?developerId=%s&operation=ItemSearch&version=2010-09-15&imageFlag=1&genreId=%s&page=%s&affiliateId=%s" % (DEV, BABY_DALL, i, AFI)).read();
    dic = json.loads(s);

    items = dic["Body"]["ItemSearch"]["Items"]["Item"];
    regist_data = [];
    filenames = [];

    for item in items:
        url = item["mediumImageUrl"];
        print "url=" + url
        url = url.replace("_ex=128x128", "_ex=256x256");
        img = urllib2.urlopen(url).read();
        filename = str(urlparse(url.split("?")[0]).path.split("/")[-1]);
        regist_data.append({"filename": str(filename), "title": item["itemName"], "url": item["affiliateUrl"]});
        f = open(filename, "wb");
        f.write(img);
        f.close();

    for r in regist_data:
        filename = r["filename"];
        title = r["title"];
        url = r["url"];
        print filename
        try:
            if (face.is_in_face(filename) == False):
                print "out";
                os.remove(filename);
            else:
                cursor.execute("SELECT COUNT(id) FROM ladys");
                new_id = cursor.fetchone()[0] + 1;
                connector.execute("INSERT INTO ladys VALUES(%s, '%s', '%s', '%s')" % (new_id, filename, title, url));
        except AttributeError:
            print "Error"
    connector.commit();

