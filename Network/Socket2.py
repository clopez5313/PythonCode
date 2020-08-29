import socket
# URL with lots of text: https://www.w3.org/Protocols/rfc2616/rfc2616.txt
# Shorter URL: http://data.pr4e.org/romeo.txt

url = input('Enter the URL - ')
fullURL = url.split('/')

try:
    host = fullURL[2]
except:
    print('The URL that you entered is not correctly formatted.')
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, 80))
except:
    print('The URL that you entered does not exist or is not available.')
    exit()

url = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
cmd = url.encode()
mysock.send(cmd)

counter = 0

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    counter += len(data)

    if counter < 3000:
        print(data.decode(),end='')

print('\n')
print('Total characters:',counter)

mysock.close()
