import os
import os.path
import numpy as np
import matplotlib.pyplot as plt


def read_latencies_file(latencies_filename):
    with open(latencies_filename, 'r') as latencies_file:
        lines = latencies_file.read().split('\n')
    packet_ns = []
    latencies_ms = []
    total_n_packets = int(lines[0])
    for line in lines[1:]:
        if len(line) == 0:
            continue
        fields = line.split(' ')
        packet_n = int(fields[0])
        packet_ns.append(packet_n)
        latency_us = float(fields[1])
        latency_ms = latency_us / 1000
        latencies_ms.append(latency_ms)
    packet_ns = np.array(packet_ns)
    latencies_ms = np.array(latencies_ms)
    return (packet_ns, latencies_ms, total_n_packets)


def draw_timeseries(packets_all_hosts, save_dir,graphname):
    plt.figure()
    plt.suptitle("Packet latency over time")
    data=[]
    data.append(packets_all_hosts)

    n_hosts = len(data)
    for board_n in range(n_hosts):
        ( packet_ns, latencies_ms,
         total_n_packets) = data[board_n]
        packet_ns = list(packet_ns)
        latencies_ms = list(latencies_ms)
        plt.subplot(n_hosts, 1, 1 + board_n)
        line=plt.plot(packet_ns, latencies_ms)[0]
        if board_n == (n_hosts - 1):
            plt.xlabel("Packet no.")
            plt.ylabel("Latency (ms)")

    plt.tight_layout()
    plt.ylim(0,10)
    plt.xlim(0, len(packet_ns))

    plot_filename = os.path.join(save_dir, graphname)
    plt.savefig(plot_filename)
    plt.show()



# # path=os.path.dirname('HD_10')
# # file_name='./HD_10'
# # print(path)
# # data=[]
# data_all_files = read_latencies_file(file_name)
# # data.append(data_all_files)
# # print(data)
#
# draw_timeseries(data_all_files,path)