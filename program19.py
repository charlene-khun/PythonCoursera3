import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('.//count')
c = 0
sum = 0
for item in results:
    c = c + 1
    sum = sum + int(item.text)
print("Count: ", c)
print("Sum: ", sum)
    
    
    
    
    
  