import pickle

res = b'1423,3423,5465,14\r\n' # 바이트 상태의 문자열
data = res.decode().split(',') #콤마로 구분된 문자열
print(type(int(data[1]))) #문자열 2번째 요소를 가져옴
send_data = [int(data[1])] * 10 # 문자열 타입인 두번째 요소를 정수형으로 바꾸고 10개 나열을 리스트에 넣어줌
dump_data = pickle.dumps(send_data) # 리스트형 그 자체를 송수신이 가능한 바이트로 주고 받을 수 있게 해줌 ( 서버에서 보내줄때 )
print(send_data)
print(dump_data)
print(pickle.loads(dump_data)) # 클라이언트에서도 받을때 마찬가지로 들어온 바이트 정보를 송신할때 자료형 그대로 받아줌