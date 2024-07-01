# Important!
# Do Not Try To Port Scan a URL for a website that you Do Not Own!

import socket
 
s = socket.socket()

# Change part "Your URL here" to the URL of a website that you own

result = s.connect_ex((YOUR_URL_HERE, 8090)) # port 8090 change to the port number you want to scan
 
if(result == 0):
  print('Port is open')
else:
  print('Port is closed')
