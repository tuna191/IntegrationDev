# #SimpleClient 
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 12345
# s.connect((host, port))
# str = "Hello,world"
# s.sendall(str.encode('utf-8')) # gửi chuỗi đến server
# data=s.recv(1024).decode('utf-8')
# print("Da nhan tt tu server",data)

# s.close()

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
server_port = 12345
client_socket.connect((host, server_port))

while True:
    response = client_socket.recv(1024).decode('utf-8')
    print(response)
    choice = input()
    client_socket.send(choice.encode())
    if choice == '1':
        data = input("Nhập chuỗi: ")
        client_socket.send(data.encode())
        result = client_socket.recv(1024).decode()
        print(f"Kết quả: {result}")
    elif choice == '2':
        data = input("Nhập chuỗi các số nguyên (cách nhau bởi khoảng trắng): ")
        client_socket.send(data.encode())
        result = client_socket.recv(1024).decode()
        print(f"Tổng các số nguyên: {result}")
    elif choice == '3':
        print("Đã ngắt kết nối.")
        break
client_socket.close()


