import  multiprocessing
exec(open("../1_Exp_Haptic_Data/datcapturing.py").read())
exec(open("../1_Exp_Haptic_Data/haptic_masterside.py").read())

# exec(open("./datcapturing.py").read()) # Uncooment and use for directly used with xterm
# exec(open("./haptic_masterside.py").read()) # Uncooment and use for directly used with xterm

if __name__ == '__main__':
    receiver = multiprocessing.Process(target=send_dataPackets)
    sender   = multiprocessing.Process(target=packet_backwarding)

    receiver.start()
    sender.start()
    receiver.join()
    sender.join()