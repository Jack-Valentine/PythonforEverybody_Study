import urllib
from BeautifulSoup import *

default_url = 'http://python-data.dr-chuck.net/known_by_Mohamad.html'
url = ''
repeat_count = 7
position = 18

for count in range(0, repeat_count):
    if url == '': url = default_url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    print tags[position - 1].get('href', None)
