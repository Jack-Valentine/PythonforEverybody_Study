import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_238826.xml '
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

countlst = tree.findall('.//count')
print 'Count:', len(countlst)
sumcount = 0;
for itms in countlst:
    sumcount += int(itms.text)

print sumcount