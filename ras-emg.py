import asyncio
import atexit
import datetime as dt
import time
import os
import pexpect
import pickle
import socket
import sys
import termios
import threading
from datetime import datetime
from select import select

import numpy as np
from bleak import BleakClient
from serial import Serial

#
class KBHit:
    def __init__(self):
        self.fd = sys.stdin.fileno()
        self.new_term = termios.tcgetattr(self.fd)
        self.old_term = termios.tcgetattr(self.fd)
        self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)
        atexit.register(self.set_normal_term)

    def set_normal_term(self):
        termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        return sys.stdin.read(1)

    def getarrow(self):
        c = sys.stdin.read(3)[2]
        vals = [65, 67, 66, 68]
        return vals.index(ord(c.decode('utf-8')))

    def kbhit(self):
        dr,dw,de = select([sys.stdin], [], [], 0)
        return dr != []


class double_socket():
    def __init__(self):
        super(double_socket, self).__init__()
        self.tcp = False
        self.box = np.ones(10) / 10
        self.windows_user_name = os.path.expanduser('~')

        self.KST = dt.timezone(dt.timedelta(hours=9))
        self.Flag = True
        self.u_count = [0] * 5
        self.d_count = [0] * 5
        self.rdata = [1, 7000, 7000, 0]
        self.UP_FLAG = True
        self.DOWN_FLAG = True
        self.check = [0]
        self.leg_move = 0
        self.leg_up = 0
        self.leg_down = 0
        self.leg = False

    def run(self):
        self.kb = KBHit()
        self.run_leg()
        self.leg_value = True
        self.ser = Serial('/dev/ttyACM0', 500000)
        self.ser.timeout = 0.01
        self.timedata = []
        while True:
            try:
                if self.ser.readable() and self.Flag and self.leg_value:
                    self.res = self.ser.readline()
                    self.data = self.res.decode().split(',')
                    self.read_data1 = [int(self.data[0])] * 10
                    self.read_data2 = [int(self.data[1])] * 10
                    self.avg1 = [sum(self.read_data1) / 10] * 10
                    self.avg2 = [sum(self.read_data2) / 10] * 10
                    self.svf1 = [np.convolve(self.read_data1[-10:], self.box, mode='same')[-1]] * 10
                    self.svf2 = [np.convolve(self.read_data2[-10:], self.box, mode='same')[-1]] * 10
                    self.sav1 = [np.convolve(self.avg1[-10:], self.box, mode='same')[-1]] * 10
                    self.sav2 = [np.convolve(self.avg2[-10:], self.box, mode='same')[-1]] * 10
                    self.timedata = [datetime.now(self.KST).strftime('%Y-%m-%d+%H_%M_%S.%f')] * 10
                    del self.read_data1[0]
                    del self.read_data2[0]
                    del self.avg1[0]
                    del self.avg2[0]
                    del self.svf1[0]
                    del self.svf2[0]
                    del self.sav1[0]
                    del self.sav2[0]
                    del self.timedata[0]

                    self.Flag = False
            except:
                print('retry....')
                continue
            break

        taddr = ''
        self.t_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.t_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.t_server.bind((taddr, 9001))
        self.t_server.listen()
        print('TCP ON')

        threading.Thread(target=self.tcp_execute).start()
        threading.Thread(target=self.binder).start()

    def binder(self):
        while True:
            try:
                if self.kb.kbhit():
                    a = ord(self.kb.getch())
                    if a == 44:
                        self.child.sendline('char-write-cmd 0x0010 0x2b525400060d')
                        print('<')
                    elif a == 46:
                        self.child.sendline('char-write-cmd 0x0010 0x2b525401070d')
                        print('>')
                # print(datetime.utcnow().strftime('%Y-%m-%d+%H_%M_%S.%f'))
                # if self.ser.readable():
                self.res = self.ser.readline()
                self.data = self.res.decode().split(',')
                self.read_data1.append(int(self.data[0]))
                self.read_data2.append(int(self.data[1]))
                self.avg1.append(sum(self.read_data1[-10:]) / 10)
                self.avg2.append(sum(self.read_data2[-10:]) / 10)
                self.svf1.append(np.convolve(self.read_data1[-10:], self.box, mode='same')[-1])
                self.svf2.append(np.convolve(self.read_data2[-10:], self.box, mode='same')[-1])
                self.sav1.append(np.convolve(self.avg1[-10:], self.box, mode='same')[-1])
                self.sav2.append(np.convolve(self.avg2[-10:], self.box, mode='same')[-1])
                self.timedata.append(datetime.now(self.KST).strftime('%Y-%m-%d+%H_%M_%S.%f'))

                self.leg_check()
                if len(self.read_data1) == 20:
                    del self.read_data1[:10]
                    if len(self.read_data2) == 19:
                        del self.read_data2[:9]
                        del self.avg1[:9]
                        del self.avg2[:9]
                        del self.svf1[:9]
                        del self.svf2[:9]
                        del self.sav1[:9]
                        del self.sav2[:9]
                        del self.timedata[:9]
                    elif len(self.read_data2) == 20:
                        del self.read_data2[:10]
                        del self.avg1[:10]
                        del self.avg2[:10]
                        del self.svf1[:10]
                        del self.svf2[:10]
                        del self.sav1[:10]
                        del self.sav2[:10]
                        del self.timedata[:10]
                    elif len(self.read_data2) == 18:
                        del self.read_data2[:8]
                        del self.avg1[:8]
                        del self.avg2[:8]
                        del self.svf1[:8]
                        del self.svf2[:8]
                        del self.sav1[:8]
                        del self.sav2[:8]
                        del self.timedata[:8]
                    #print(len(self.read_data1), len(self.read_data2), len(self.avg1), len(self.avg2), len(self.svf1), len(self.svf2), len(self.sav1), len(self.sav2))
                    if self.tcp:
                        try:
                            self.recv_data = self.t_client.recv(200000)
                            self.rdata = pickle.loads(self.recv_data)
                            # print(self.rdata[3])
                            if int(self.rdata[3]) == 1:
                                self.run_leg()
                            elif int(self.rdata[3]) == 2:
                                self.stop_leg()
                            elif int(self.rdata[3]) == 3:
                                self.l_test()
                            self.t_client.send(pickle.dumps(
                                [self.read_data1, self.avg1, self.svf1, self.sav1, self.read_data2,
                                 self.avg2, self.svf2, self.sav2,
                                 self.timedata, self.leg_move]))
                        except:
                            self.t_client.close()
                            self.tcp = False
                            print('Except TCP')
                # print('{:.2f}'.format(self.read_data1[-1]) + '\t' + '{:.2f}'.format(
                #     self.read_data2[-1]) + '\t' + '{:.2f}'.format(self.avg1[-1]) + '\t' + '{:.2f}'.format(
                #     self.avg2[-1]) + '\t' + '{:.2f}'.format(self.svf1) + '\t' + '{:.2f}'.format(
                #     self.svf2) + '\t' + '{:.2f}'.format(self.sav1) + '\t' + '{:.2f}'.format(
                #     self.sav2) + '\t' + str(self.rdata[1]) + '\t' + str(self.rdata[2]) + '\t' + str(self.leg_move))

            except:
                pass

    def leg_check(self):
        if self.rdata[0] == 1:
            if self.read_data1[-1] >= self.rdata[1]:
                self.u_count.append(1)
                del self.u_count[0]
            else:
                self.u_count.append(0)
                del self.u_count[0]
            if self.read_data2[-1] >= self.rdata[2]:
                self.d_count.append(1)
                del self.d_count[0]
            else:
                self.d_count.append(0)
                del self.d_count[0]
            if self.read_data1[-1] >= self.rdata[1] and self.UP_FLAG == True and sum(self.u_count) == 1 and self.u_count[-1] == 1:
                self.UP_FLAG = False
                self.leg_up = 1
            elif self.read_data1[-1] < self.rdata[1] and sum(self.u_count) == 4 and self.u_count[-1] == 0:
                self.UP_FLAG = True
                self.leg_up = 0
            if self.read_data2[-1] >= self.rdata[2] and self.DOWN_FLAG == True and sum(self.d_count) == 1 and self.d_count[-1] == 1:
                self.DOWN_FLAG = False
                self.leg_down = 1
            elif self.read_data2[-1] < self.rdata[2] and sum(self.d_count) == 4 and self.d_count[-1] == 0:
                self.DOWN_FLAG = True
                self.leg_down = 0
        elif self.rdata[0] == 2:
            if self.avg1[-1] >= self.rdata[1]:
                self.u_count.append(1)
                del self.u_count[0]
            else:
                self.u_count.append(0)
                del self.u_count[0]
            if self.avg2[-1] >= self.rdata[2]:
                self.d_count.append(1)
                del self.d_count[0]
            else:
                self.d_count.append(0)
                del self.d_count[0]
            if self.avg1[-1] >= self.rdata[1] and self.UP_FLAG == True and sum(self.u_count) == 1 and self.u_count[-1] == 1:
                self.UP_FLAG = False
                self.leg_up = 1
            elif self.avg1[-1] < self.rdata[1] and sum(self.u_count) == 4 and self.u_count[-1] == 0:
                self.UP_FLAG = True
                self.leg_up = 0
            if self.avg2[-1] >= self.rdata[2] and self.DOWN_FLAG == True and sum(self.d_count) == 1 and self.d_count[-1] == 1:
                self.DOWN_FLAG = False
                self.leg_down = 1
            elif self.avg2[-1] < self.rdata[2] and sum(self.d_count) == 4 and self.d_count[-1] == 0:
                self.DOWN_FLAG = True
                self.leg_down = 0
        elif self.rdata[0] == 3:
            if self.svf1[-1] >= self.rdata[1]:
                self.u_count.append(1)
                del self.u_count[0]
            else:
                self.u_count.append(0)
                del self.u_count[0]
            if self.svf2[-1] >= self.rdata[2]:
                self.d_count.append(1)
                del self.d_count[0]
            else:
                self.d_count.append(0)
                del self.d_count[0]
            if self.svf1[-1] >= self.rdata[1] and self.UP_FLAG == True and sum(self.u_count) == 1 and self.u_count[-1] == 1:
                self.UP_FLAG = False
                self.leg_up = 1
            elif self.svf1[-1] < self.rdata[1] and sum(self.u_count) == 4 and self.u_count[-1] == 0:
                self.UP_FLAG = True
                self.leg_up = 0
            if self.svf2[-1] >= self.rdata[2] and self.DOWN_FLAG == True and sum(self.d_count) == 1 and self.d_count[-1] == 1:
                self.DOWN_FLAG = False
                self.leg_down = 1
            elif self.svf2[-1] < self.rdata[2] and sum(self.d_count) == 4 and self.d_count[-1] == 0:
                self.DOWN_FLAG = True
                self.leg_down = 0
        elif self.rdata[0] == 4:
            if self.sav1[-1] >= self.rdata[1]:
                self.u_count.append(1)
                del self.u_count[0]
            else:
                self.u_count.append(0)
                del self.u_count[0]
            if self.sav2[-1] >= self.rdata[2]:
                self.d_count.append(1)
                del self.d_count[0]
            else:
                self.d_count.append(0)
                del self.d_count[0]
            if self.sav1[-1] >= self.rdata[1] and self.UP_FLAG == True and sum(self.u_count) == 1 and self.u_count[-1] == 1:
                self.UP_FLAG = False
                self.leg_up = 1
            elif self.sav1[-1] < self.rdata[1] and sum(self.u_count) == 4 and self.u_count[-1] == 0:
                self.UP_FLAG = True
                self.leg_up = 0
            if self.sav2[-1] >= self.rdata[2] and self.DOWN_FLAG == True and sum(self.d_count) == 1 and self.d_count[-1] == 1:
                self.DOWN_FLAG = False
                self.leg_down = 1
            elif self.sav2[-1] < self.rdata[2] and sum(self.d_count) == 4 and self.d_count[-1] == 0:
                self.DOWN_FLAG = True
                self.leg_down = 0
        if self.leg_up == 1 and self.leg_down == 1:
            self.check.append(1)
            if self.check[0] == self.check[-1]:
                self.leg_move = 0
            else:
                self.leg_move = 1
                if self.leg:
                    self.l_up()
            del self.check[0]
        elif self.leg_up == 0 and self.leg_down == 1:
            self.check.append(2)
            if self.check[0] == self.check[-1]:
                self.leg_move = 0
            else:
                self.leg_move = 2
                if self.leg:
                    self.l_down()
            del self.check[0]
        else:
            self.leg_move = 0


    def tcp_execute(self):
        try:
            while True:
                self.t_client, self.taddr = self.t_server.accept()
                self.tcp = True
                print('TCP Connected by', self.taddr)
        except:
            print("TCP Except")
            self.tcp = False
        finally:
            self.t_server.close()
            self.tcp = False
            print("TCP Server Done...")


    def run_leg(self):
        scan = pexpect.spawn("sudo hcitool lescan")
        time.sleep(5)
        print(scan.terminate())

        # self.child = pexpect.spawn("sudo gatttool -i hci0 -b 5c:f2:86:41:9b:bf -I")
        self.child = pexpect.spawn("sudo gatttool -i hci0 -b 5c:f2:86:41:96:f4 -I")
        print(self.child.sendline("connect"))
        self.leg = True


    def stop_leg(self):
        self.child.sendline("disconnect")
        self.child.sendline("exit")
        self.leg = False

    def l_up(self):
        self.child.sendline('char-write-cmd 0x0010 0x2b525401070d')

    def l_test(self):
        self.child.sendline('char-write-cmd 0x0010 0x2b525401070d')

    def l_down(self):
        self.child.sendline('char-write-cmd 0x0010 0x2b525400060d')

if __name__ == '__main__':
    print('Start Server')
    two_socket = double_socket()
    two_socket.run()

