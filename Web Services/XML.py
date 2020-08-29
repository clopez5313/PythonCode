import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
#URL: http://py4e-data.dr-chuck.net/comments_42.xml
#URL: http://py4e-data.dr-chuck.net/comments_461617.xml

data = urllib.request.urlopen(address, context=ctx).read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
comtree = tree.find('comments')
total = 0

for comment in comtree :
    ctree = comtree.find('comment')

    for child in comment :

        if child.tag == 'count' :
            tot = int(child.text)
            total = total + tot

print("Sum:", total)
