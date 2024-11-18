
'''
소켓통신에서 서버는 보통 최초의 수신자가 되는 노드를 의미한다. 따라서 서버는 소켓을 만들고 포트에 맵핑한 다음, 클라이언트가 접속하기를 기다리게 된다. 
서버가 소켓을 포트에 맵핑하는 행위를 바인딩이라 하며, 이는 생성된 소켓 객체에 대해서 sock.bind() 메소드를 호출한다. 
bind() 호출 시에는 호스트이름과 포트번호를 튜플로 감싸서 전달한다

바인드는 프로그램 인터페이스인 소켓과 네트워크 자원인 포트를 연결하는 행위이다. 따라서 프로그래머는 자신이 사용하는 포트가 명시적으로 몇 번인지, 
자신의 IP가 무엇인지 알고 있어야 한다. (알고 있다는 말은 즉 자신이 능동적으로 정해준다는 말이다.)

바인드가 완료된 후 수행해야 하는 동작은 리스닝이다. 이는 소켓에 대해 listen() 메소드를 호출하여 수행한다. 
이 메소드는 클라이언트가 바인드된 포트로 연결을 할 때까지 기다리는 블럭킹 함수이다. 
클라이언트로부터 연결 요청이 들어오면 리턴하게 되는데, 
따라서 이 코드의 다음 행에는 해당 연결을 받아들이기 위한 accecpt() 메소드를 호출하는 부분이 주로 오게 된다.

accept()는 (소켓, 주소정보)로 구성되는 튜플을 리턴한다. 
이때의 소켓은 처음에 생성한 소켓과는 별개의 객체로 클라이언트와 연결이 구성되어 실제로 데이터를 주고 받을 수 있는 창구가 된다. 
이 소켓은 연결이 들어와서 listen(), accept() 가 호출될 때마다 생성될 수 있기 때문에 만약, 연결이 구성된 소켓을 멀티스레드로 처리한다면 1:N의 연결도 처리할 수 있다.

소켓 역시 외부 리소스를 열어서 사용하는 것이므로 닫는 것이 매우 중요하다. 연결을 종료할 때에는 서버와 클라이언트 모두 소켓을 닫아야 하며, 
이미 닫혀있는 소켓에서 데이터를 받으려하거나 데이터를 보내려하는 동작은 모두 에러가 된다. 
소켓을 닫을 때에는 sock.close() 메소드를 사용한다.
 참고로 소켓 객체는 컨텍스트 매니저 프로토콜을 지원하므로 with 구문과 함께 사용하면 안전하게 닫히는 것을 보장할 수 있다.
'''

import socket
from serial import Serial
import threading
import pickle
import time
import random

def bind_IP_PO(client_socket, addr):
    sPort = 3  # Ui를 만드는 경우 3대신 해당 포트 번호 입력받는 self.object
    ser = Serial("com" + str(sPort), 500000)  # 회준형께 500000부분을 아두이노 IDE에서 어떻게 설정하는지 질문해볼 것
    print("serial open")
    print('Connected by', addr)
    read_data = []
    try:
        if ser.readable():
            print("r_able")
            while True:
                res = ser.readline()
                # print(res)
                data = res.decode().split(',')# 들어오는 센서신호를 디코딩 해줌/ (',')는 콤마 넣어주는건가?
                print(data)
                # read_data = [data[1]]
                # read_data.append(data[1]) # 바이트 데이터를 디코딩한 두번째 인자값을 리스트 자료형으로 변수에 넣어줌
                # # print("a_able")
                #
                # if len(read_data) == 11:
                #     del read_data[0]
                #
                #     print(read_data)

                r_data = pickle.dumps(read_data)
                client_socket.send(r_data)
    except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
        print('조깡.', e)
        print("except : ", addr)  # 접속 끊기면 expert 처리
    finally:
        client_socket.close()

def execute():
    try:
        while True:
            client_socket, addr = server_socket.accept()
            bind_IP_PO(client_socket, addr)
    except:
        print("?")
    finally:
        server_socket.close()
        print("DOwn ser")

if __name__ == '__main__':
    print('Start Server')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 50002))  # 포트 설정 부분
    server_socket.listen(1)

    my_thread = threading.Thread(target=execute)
    my_thread.start()