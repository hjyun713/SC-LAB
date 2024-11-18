from serial import Serial


#포트번호 연결 요청 Trigger
sPort = 3  # Ui를 만드는 경우 3대신 해당 포트 번호 입력받는 self.object
ser = Serial("com" + str(sPort), 500000)  # 회준형께 500000부분을 아두이노 IDE에서 어떻게 설정하는지 질문해볼 것
try:
    if ser.readable():
        read_data = []
        r_data = []
        while True:
            res = ser.readline()
            # print(res)
            data = res.decode().split(',') #들어오는 센서신호를 디코딩 해줌/ (',')는 콤마 넣어주는건가?
            print(data)
            # read_data.append(data[1]) # 바이트 데이터를 디코딩한 두번째 인자값을 리스트 자료형으로 변수에 넣어줌
            #
            #
            # if len(read_data)==11:
            #
            #
            #
            #     del read_data[0]
            #
            #     print(read_data)


except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
    print('조깡.', e)






