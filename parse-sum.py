__author__ = 'MJR2'

__author__ = 'MJR2'

import urllib
from BeautifulSoup import *

url ='http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_193707.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup.findAll('span')

sum = 0
for tag in tags:
    temp = tag.text
    if temp is not None:
        sum = sum + int(temp)
print sum