#SimpleServer.py 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() # lấy địa chỉ ip hiện tại của máy 
port = 12345 
s.bind((host, port)) # chỉ định kết nối đến host và port
s.listen(5) # số lượng hàng chờ
while True:
    c, addr = s.accept() # đưa server vào trạng thái chờ đợi cho đến khi có một client kết nối tới port mà bạn đã xác định
    print("Da chap nhan ket noi tu ", addr)

      # Nhận dữ liệu từ client
    data = c.recv(1024).decode('utf-8')
    print(f"Nhận từ client: {data}")
   
    # Gửi dữ liệu trả lại cho client
    
    c.send(data.encode('utf-8'))

      
    c.close()