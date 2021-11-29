import socket, time, pickle
import multiprocessing

exec(open("../1_Exp_Haptic_Data/settings.txt").read()) #TODO use to run with CMD in mininet command using maketerm
#exec(open("./settings.txt").read()) # Uncooment and use for directly used with xterm

listen_port=kin_link_1
n_packets_expected= n_packets
target_ip=PC_2

def packet_forwarding():
    sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_in.bind(("0.0.0.0", listen_port))
    print("Slave running...")
    while True:
        try:
            data, recv_addr = sock_in.recvfrom(1024)
            if not data:
                break
            send_addr = (target_ip, listen_port + 1)
            sock_in.sendto(data, send_addr)
            print(f"B-->Slave <--- {data}, {len(data)}")  # TODO
            # sock_in.sendall(data) # TODO for sent all
        except KeyboardInterrupt:
            print("Slave in Exception mode") # TODO
            break
    print("Closing...")
    sock_in.close()

# packet_backwarding()
if __name__ == '__main__':
    receiver = multiprocessing.Process(target=packet_forwarding)
#     # receiver = multiprocessing.Process(target=packet_recieve(listen_port))
#
    receiver.start()
#     # receiver.start()
#
    receiver.join()
#     # receiver.join()