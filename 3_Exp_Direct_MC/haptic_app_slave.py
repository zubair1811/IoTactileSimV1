import math
import sys
import time
from mininet.log import info
import sim
import socket, pickle
import libfunctions as code

exec(open("../3_Exp_Direct_MC/settings.txt").read())


listen_port=kin_link_1
n_packets_expected= n_packets
target_ip=PC_2

info('Program started')
sim.simxFinish(-1)  # just in case, close all opened connections
clientID = sim.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to CoppeliaSim
if clientID != -1:
    info('Connected to remote API server')
else:
    info('Failed connecting to remote API server')
    sys.exit('Error in connecting')

sim.simxAddStatusbarMessage(clientID, 'Hello CoppeliaSim!', sim.simx_opmode_oneshot)
errorcode, jointHandle = sim.simxGetObjectHandle(clientID, 'Revolute_joint', sim.simx_opmode_blocking)

def Recieved_controlSignals():
    sock_in = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_in.bind(("0.0.0.0", listen_port))
    print("Slave running...")
    while True:
        data, recv_addr = sock_in.recvfrom(1024)
        print(f"F-->Slave <--- {data}, {len(data)}")
        data_list = code.decode(data.decode())
        new_data = code.mapping(data_list)
        print(f" {new_data} , with datatype {type(new_data)}")
        sim.simxSetJointTargetPosition(clientID, jointHandle, new_data * math.pi / 180, sim.simx_opmode_streaming)
    sim.simxFinish(clientID)
    sock_in.close()

if __name__ == '__main__':
    Recieved_controlSignals()
