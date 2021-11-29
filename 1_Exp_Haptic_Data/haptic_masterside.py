import socket, time, pickle
import multiprocessing

exec(open("../1_Exp_Haptic_Data/settings.txt").read())  #TODO use to run with CMD in mininet command using maketer
#exec(open("./settings.txt").read()) # Uncooment and use for directly used with xterm

target_ip = PC_2 #10.0.0.2
listen_port=kin_link_0 #6000
target_address=(target_ip,listen_port)
packet_len=packet_len
n_packets=n_packets
n_packets_expected= n_packets
send_rate_kbytes_per_s=send_rate_kbytes_per_s


def save_packet_latencies(packetn_latency_tuples, n_packets_expected, output_filename):
        path ='../1_Exp_Haptic_Data/HD_latencyfiles/%s'%output_filename
        with open(path, 'w') as out_file:
            out_file.write("%d\n" % n_packets_expected)
            for tup in packetn_latency_tuples:
                packet_n = tup[0]
                latency = "%.2f" % tup[1]
                out_file.write("%s %s\n" % (packet_n, latency))

def packet_backwarding():
    sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_in.bind(("0.0.0.0", listen_port+3))
    print("B_Server running...")
    packets=[]
    while len(packets)<n_packets_expected:
        data = sock_in.recv(125)
        print(f"B_Master<--- {data}")
        recv_time = time.time()
        payload = data.rstrip("a".encode())  # TODO
        (packet_n, send_time) = pickle.loads(payload)
        latency_us = (recv_time - send_time) * 1e6
        packets.append((packet_n, latency_us))
    print("Done !!!!")
    output_filename = "HD_{}".format(n_packets_expected)
    save_packet_latencies(packets, n_packets_expected, output_filename)
    print("Closing...")
    sock_in.close()
