import re
def code(my_list):
    my_list_str = map(str, my_list)
    msg = " ".join(my_list_str)
    msg = "B" + " " + msg + " " + "E"
    return (msg)


def codev2(msg, msg_list):
    msg_list_str = map(str, msg_list)
    temp1 = " ".join(msg_list_str)
    temp1 = "B" + " " + temp1 + " " + "E"
    # print temp1
    result = re.sub(r'(B(.+?)E)', temp1, msg)
    return (result)


def decode(msg):
    if (re.search('B (.+?) E', msg)):
        str = re.search('B (.+?) E', msg).group(1)
    else:
        str = "NaN"
    myArray = str.split(" ")
    return (myArray)

def mapping(mahlist):
    x = int(mahlist[0])
    # y = mahlist[1]
    x_new = (x - 0) * (360 - 0) / (1919 - 0) + 0
    return x_new

