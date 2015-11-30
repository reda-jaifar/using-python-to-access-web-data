__author__ = 'MJR2'
import xml.etree.ElementTree as ET
import urllib

xml_data_location = raw_input('Location: ')
data = urllib.urlopen(xml_data_location).read()

root = ET.fromstring(data)
counts = root.findall('.//count')
sum = 0
for item in counts:
    sum += int(item.text)

print sum