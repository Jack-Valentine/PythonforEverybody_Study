import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/comments_238830.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()

info = json.loads(data)
print 'Count:', len(info['comments'])
totla_count = 0;
for item in info['comments']:
    totla_count += item['count']
print totla_count