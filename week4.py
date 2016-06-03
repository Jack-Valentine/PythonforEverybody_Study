import urllib
from BeautifulSoup import *

# url = raw_input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_238829.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
total_count = 0
total_sum = 0

for tag in tags:
    total_count = total_count + 1
    total_sum = total_sum + int(tag.contents[0])

print 'Count ', total_count
print 'Sum ', total_sum