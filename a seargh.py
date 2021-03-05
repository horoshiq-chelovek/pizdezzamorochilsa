import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
ip = s.getsockname()[0]
s.close()



def scan_port(ip,port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)
  try:
     connect = sock.connect((ip,port))
     print('Port :',port,' its open.')
     connect.close()
  except:
     pass
ip = '185.3.68.225'
for i in range(1000):
  scan_port(ip,i)