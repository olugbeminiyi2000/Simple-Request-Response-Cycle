#!/usr/bin/python3
import socket

# make the internet file which we can open
# inorder to retrieve and send data
# but first we have to open the file for connection
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# make the phone call to the server using the domain name and port number
# i.e make the connection after it has been opened
mysock.connect(('localhost', 9000))

# now after the connection has been made give me the request headers
# to be sent through this connection but encode it using .encode()
cmd = "GET http://127.0.0.1/postgres/postgres.tery HTTP/1.0\r\n\r\n".encode()

# now send the header to the server
mysock.send(cmd)

# now wait for the server until so number of bytes is retrieved and if
# retrieved decode the utf-8 char to unicode char, because python prints
# out unicode characters because all chars in py are unicode.
# then print it out but still go again till no data is retrieved
while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
  print(data.decode(), end='')

# now close the connection
mysock.close()
