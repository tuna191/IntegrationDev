#SimpleClient 
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))
str = "Hello, world!"
s.sendall(str.encode('utf-8')) # gửi chuỗi đến server
data=s.recv(1024).decode('utf-8')
print("Da nhan tt tu server",data)

s.close()