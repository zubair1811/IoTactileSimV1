import socket, sys
import multiprocessing

exec(open("../1_Exp_Haptic_Data/settings.txt").read())  #TODO use to run with CMD in mininet command using maketerm
#exec(open("./settings.txt").read()) # Uncooment and use for directly used with xterm

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
            # print(f"F_Server ---> {data}, {len(data)}") # TODO
            if not data:
                break
            # send_addr = (target_ip, listen_port + 1)
            # sock_out.sendto(data, send_addr)
            sock_out.sendall(data) # TODO for sent all
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
#
    receiver.start()
    sender.start()
#
#     receiver.terminate()
#     sender.terminate()
#
    receiver.join()
    sender.join()