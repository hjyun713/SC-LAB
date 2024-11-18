import socket
from matplotlib import pyplot
import pickle
import time

'''
TCP>>>
소켓으로부터 데이터를 읽을 때는 sock.recv()를, 정보를 보낼 때는 sock.sendall()을 사용한다. 
데이터를 읽어들일 때에는 버퍼의 크기를 전달해야 한다. 
sock.recv(bufsize)는 최대 bufsize 바이트만큼의 데이터를 읽어온다. 
만약 읽어들일 데이터가 아예 없다면 상대방이 데이터를 보내줄때까지 대기한다.

읽어들인 데이터는 bytes 타입의 바이트 시퀀스이며, 데이터를 보낼때에도 바이트시퀀스를 보내야 한다. 
만약 문자열을 주고 받고 싶다면 해당 문자열을 인코딩/디코딩해서 전달해야 한다.

클라이언트가 서버와 통신하는 방법도 거의 비슷하다, 다만 한가지 차이점이 있다면 클라이언트는 바인드나 리스닝의 과정이 필요없다는 것이다. 
클라이언트는 능동적으로 서버에 연결하며, 연결된 소켓으로 항상 1:1로 서버와 통신하기 때문이다. 
(물론 이것은 클라이언트의 입장이다. 결국 서버가 바인딩이 필요한 이유는 같은 포트로 여러 클라이언트와 동시에 접속될 수 있기 때문이다.)
'''

IP = '192.168.2.51'
PORT = 50002

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    while True:
        s.sendall(b'pre') #서버에게 통신요청 (바이트 화) 인코딩
        data = s.recv(1024) #서버로부터 응답받기
        wqwq = pickle.dumps(data) # 서버로부터 온 바이트 응답 디코드 해줌
        print(wqwq)
        # qw = [int(i) for i in wqwq]
        # pyplot.title("zotka")
        # pyplot.grid()
        # pyplot.plot([range(1, 10)], wqwq)
        # pyplot.show()




except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
    print('조깡.', e)
finally:
    print("ㅃㅃ2")

