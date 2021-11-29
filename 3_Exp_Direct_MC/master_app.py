import time
import pickle
import socket
from pynput.mouse import Button,Controller
mouse=Controller()

exec(open("../3_Exp_Direct_MC/settings.txt").read())
target_ip = PC_2  # 10.0.0.2
listen_port = kin_link_0  # 6000
target_address = (target_ip, listen_port)
n_packets=n_packets
n_packets_expected= n_packets

def get_packet_payload(packet_n):
    send_time_seconds = time.time()
    payload = pickle.dumps((packet_n, send_time_seconds),0).decode()
    return payload

def message_format(axis_x,axis_y):
    msg = "B "+ str(axis_x)
    msg = msg + " " + str(axis_y)
    msg = msg + " E\n"
    return(msg)

def send_controlSignal():
    socket_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_out.connect(target_address)
    while True:
        postion = mouse.position
        axis_x = postion[0]
        axis_y = postion[1]
        payload = message_format(axis_x, axis_y)
        msg = payload.encode()
        print(f"Move---> {msg}")
        socket_out.sendall(msg)
    socket_out.close()

if __name__ == '__main__':
    send_controlSignal()


