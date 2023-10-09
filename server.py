import socket
import threading

def reverse_and_capitalize(data):
    reversed_words = data[::-1].lower().title()
    return reversed_words

def calculate_sum(data):
    numbers = [int(num) for num in data.split() if num.isdigit()] #isdigit == isNumber()
    return sum(numbers)

def handle_client(client_socket):
    try:
        while True:
            client_socket.send("\n1. Đảo ngược chuỗi và in hoa ký tự đầu của mỗi từ\n2. Tính tổng các số nguyên\n3. Thoát\nNhập lựa chọn: ".encode())
            choice = client_socket.recv(1024).decode()
            
            if choice == '1':
                data = client_socket.recv(1024).decode()
                result = reverse_and_capitalize(data)
                client_socket.send(result.encode())
            elif choice == '2':
                data = client_socket.recv(1024).decode()
                result = str(calculate_sum(data))
                client_socket.send(result.encode())
            elif choice == '3':
                break
    except Exception as e:
        print(f"Lỗi: {e}")
    finally:
        client_socket.close()

server_ip = socket.gethostname()
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)

print(f"Server đang lắng nghe trên {server_ip}:{server_port}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Kết nối từ: {client_address}")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
