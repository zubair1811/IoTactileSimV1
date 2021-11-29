import socket, sys
import multiprocessing
import libfunctions as code
exec(open("../2_Exp_Mouse_VREP_Feedback/settings.txt").read())
# exec(open("./settings.txt").read())

listen_port=kin_link_0
target_ip=PC_3
b_target_ip= PC_1
def packet_forwarding():
    sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_in.bind(("0.0.0.0", listen_port))
    sock_out = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    send_addr = (target_ip, listen_port + 1)# TODO for sent all
    sock_out.connect(send_addr)  # TODO for sent all
    print("Server running...")
    while True:
        try:
            data, recv_addr = sock_in.recvfrom(1024)
            data_list=code.decode(data.decode())
            # print(f"F_Server ---> {data_list}, {len(data)}") # TODO
            data=code.codev2(data.decode(),data_list)
            # print(f"Decoding--{data}")
            sock_out.sendall(data.encode()) # TODO for sent all
        except KeyboardInterrupt:
            print("Server in Exception mode") # TODO
            break
    print("Closing...")
    sock_out.close()
    sys.exit(0)


def packet_backwarding():
    sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_in.bind(("0.0.0.0", listen_port+2))
    print("B_Server running...")
    while True:
        try:
            data, recv_addr = sock_in.recvfrom(1024)
            # print(f"B-Server <--- {data}, {len(data)}")
            if not data:
                break
            send_addr = (b_target_ip, listen_port + 3)
            sock_in.sendto(data, send_addr)
            print(f"B-Server <--- {data}, {len(data)}")  # TODO
            # sock_in.sendall(data) # TODO for sent all
        except KeyboardInterrupt:
            print("Server in Exception mode") # TODO
            break
    print("Closing...")
    sock_in.close()




if __name__ == '__main__':
    receiver = multiprocessing.Process(target=packet_forwarding)
    sender = multiprocessing.Process(target=packet_backwarding)

    receiver.start()
    sender.start()
    receiver.join()
    sender.join()