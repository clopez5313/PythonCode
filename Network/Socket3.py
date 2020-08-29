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
headersEnd = 0
started = False
text = None

while True:
    data = mysock.recv(512)

    if len(data) < 1:
        break

    str = data.decode()

    if not started:
        headersEnd = str.find('\r\n\r\n')

        if headersEnd <= 0 and not started:
            continue
        elif headersEnd > 0 and not started:
            started = True
            text = str[headersEnd+4:]
            counter = counter + len(text)
            continue
            
    if counter < 3000:
        text = text + str

    counter = counter + len(str)

print(text)
print('\b')
print('Total characters:',counter)

mysock.close()
