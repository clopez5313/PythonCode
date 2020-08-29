import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
print('Retrieving:', url)
print('\b')

try:
    html = urllib.request.urlopen(url, context=ctx).read()
except:
    print('The URL that you entered is not correctly formatted, does not exists, or is not available.')
    exit()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('p')
counter = 0

for tag in tags:
    counter += 1

print('The total of <p> tags was:', counter)
