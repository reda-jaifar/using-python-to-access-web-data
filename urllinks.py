# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

def get_link_at(url, index):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    link = tags[int(index)]
    return link

# Enter the main url
entry_url = raw_input('URL:')
position = raw_input('Link position: ')
repeat = raw_input('Repeat: ')
position = int(position) - 1

result = get_link_at(entry_url, position)

for ite in range(1, int(repeat)):
    result = get_link_at(result.get('href', None), position)

print result.text

