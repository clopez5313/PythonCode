import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
#URL: http://py4e-data.dr-chuck.net/comments_42.json
#URL: http://py4e-data.dr-chuck.net/comments_461617.json
data = urllib.request.urlopen(address, context=ctx).read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
item = info['comments']
total = 0

for i in item :
    num = int(i['count'])
    total = total + num

print('Sum:', total)
