# import socket
# import threading
# import serial
# import random
# import time
#
# def binder(client_socket, addr):
#     print('Connected by', addr)
#     time.sleep(2)
#     try:
#         while True:
#             time.sleep(2)
#             data = str(random.randint(0,3))
#             print(data)
#             encode_data = str(data + '\r').encode()
#             client_socket.send(encode_data)
#             # tcp_get = client_socket.recv(1024) //
#             # print(tcp_get)
#     except socket.error as e:
#         print("Socket error: {}".format(str(e)))
#     finally:
#         client_socket.close()
#
#
#
# def execute():
#     try:
#         while True:
#             client_socket, addr = server_socket.accept()
#             # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#             # client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 10)
#             # client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 5)
#             binder(client_socket, addr)
#
#     except:A
#         print("holly molly")
#
#     finally:
#         server_socket.close()
#         print("Server Done")
#
#
#
# if __name__ == "__main__":
#     print('server start')
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.bind(('', 50002))
#     server_socket.listen()
#
#     my_thread = threading.Thread(target=execute)
#     my_thread.start()

import socket
import threading
import random
import time


def binder(client_socket, addr):
    print('Connected by', addr)
    time.sleep(2)
    try:
        while True:
            time.sleep(2)
            data = str(random.randint(0, 3))
            print(f"Sending data: {data} to {addr}")
            encode_data = str(data + '\r').encode()
            print(encode_data)
            client_socket.send(encode_data)
    except socket.error as e:
        print("Socket error: {}".format(str(e)))
    finally:
        client_socket.close()


def execute(server_socket):
    try:
        while True:
            client_socket, addr = server_socket.accept()
            thread = threading.Thread(target=binder, args=(client_socket, addr))
            thread.start()
    except Exception as e:
        print(f"Exception in execute function: {e}")
    finally:
        server_socket.close()
        print("Server Done")


if __name__ == "__main__":
    print('Server starting on ports 50002 and 50003')

    # First server socket for port 50002
    server_socket_50002 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_50002.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket_50002.bind(('', 50002))
    server_socket_50002.listen()

    # Second server socket for port 50003
    server_socket_50003 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket_50003.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket_50003.bind(('', 50003))
    server_socket_50003.listen()

    # Create threads to handle both ports
    thread_50002 = threading.Thread(target=execute, args=(server_socket_50002,))
    thread_50003 = threading.Thread(target=execute, args=(server_socket_50003,))

    # Start both threads
    thread_50002.start()
    thread_50003.start()

    # Wait for both threads to finish
    thread_50002.join()
    thread_50003.join()

    print('Server Done')


