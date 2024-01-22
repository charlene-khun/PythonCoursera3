import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter url: ')

print("Retrieiving: ", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)

count1 = 0
sum = 0
for item in info['comments']:
    count1 = count1 + 1
    sum = sum + int(item['count'])
print('Count: ', count1)
print('Sum: ', sum)
    