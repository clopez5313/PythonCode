import urllib.request
# URL with lots of text: https://www.w3.org/Protocols/rfc2616/rfc2616.txt
# Shorter URL: http://data.pr4e.org/romeo.txt

url = input('Enter the URL - ')
fullURL = url.split('/')

try:
    host = fullURL[2]
except:
    print('The URL that you entered is not correctly formatted.')
    exit()

try:
    handle = urllib.request.urlopen(url)
except:
    print('The URL that you entered does not exist or is not available.')
    exit()

counter = 0

for line in handle:
    words = line.decode().strip()
    counter += len(words)

    if counter < 3000:
        print(words)

print('\n')
print('Total characters:',counter)
