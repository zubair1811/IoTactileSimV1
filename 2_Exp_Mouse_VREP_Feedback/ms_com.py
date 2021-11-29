import  multiprocessing
import time,sys
# exec(open("./master_app.py").read())
# exec(open("./ms_bwd_haptic.py").read())


exec(open("../2_Exp_Mouse_VREP_Feedback/master_app.py").read())
exec(open("../2_Exp_Mouse_VREP_Feedback/ms_bwd_haptic.py").read())

if __name__ == '__main__':
    receiver = multiprocessing.Process(target=send_controlSignal)
    sender   = multiprocessing.Process(target=packet_backwarding)

    receiver.start()
    sender.start()
    receiver.join()
    sender.join()