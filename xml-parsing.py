__author__ = 'MJR2'
import xml.etree.ElementTree as ET

data = '''
<person>
    <name>reda</name>
    <phone type="intl">+33 95 78 04 12</phone>
    <email hide="yes" />
</person>
'''

tree = ET.fromstring(data)
print 'Name: ', tree.find('name').text
print 'Attr: ', tree.find('email').get('hide')