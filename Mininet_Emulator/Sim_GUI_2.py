import PySimpleGUI as sg
import os
import graph_plot as ploting

sg.theme('DefaultNoMoreNagging')
# #---------------- Windiw layout----

mini_frame1=[
    [sg.Button('10'), sg.Button('100'),sg.Button('1000'), sg.Button('10000')]
]
mini_frame2=[
    [sg.Button('HD-10',button_color=('white','green')), sg.Button('HD-100',button_color=('white','green')),sg.Button('HD-1000',button_color=('white','green')), sg.Button('HD-10000',button_color=('white','green'))]
]

mini_frame3=[
    [sg.Button('MD-10'), sg.Button('MD-100'),sg.Button('MD-1000'), sg.Button('MD-10000')]
]

Frame_layout=[
      # [sg.Text('Start Network Simulation'), sg.Button('Start Simulation'),],
      # [sg.Text('Haptic Data'), sg.Button('EXP#1'),sg.Text('Mouse_Control'), sg.Button('EXP#2')],
      [sg.Frame('Select No. of Packets', mini_frame1, font='Any 12', title_color='blue', element_justification='center')],
      [sg.Frame('Dispaly Latency-Graph for Exp#1', mini_frame2, font='Any 12', title_color='green', element_justification='center',)],
      [sg.Frame('Dispaly Latency-Graph for Exp#2', mini_frame3, font='Any 12', title_color='blue', element_justification='center')],
      [sg.Text('Stop Simulation'), sg.Button('Exit Mininet')]
]
mainlayput=[
      [sg.Text('Wellcome to Tactile Industrial IoT Testbed', size=(90, 1), justification='center',
               background_color='light blue', text_color='red', font='10')],
      [sg.Frame('Experiment Parameter Selection', Frame_layout, font='Any 12', title_color='black',element_justification='left')],
      # [sg.Image(r'./Sejong.png')]
]

window = sg.Window(title="IoTactileSim Testbed", layout=mainlayput, size=(450, 320),
                         location=(700, 200),
                         font=('Helvetica', 12), element_justification='center')
def send():
    while True:
        event, values = window.Read()
        yield event
    window.close()








# print(list_of_lines)
# event1=next(send())
# if event1 == 'Start Simulation':
#       print("Start")
# event2=next(send())
# if event2 == 'EXP#1':
#       print("EXP#1")

def select_packet_HD():
    with open("../1_Exp_Haptic_Data/settings.txt", "r") as file:
        line_no = file.readlines()
    with open("../1_Exp_Haptic_Data/settings.txt", "r") as file:
        list_of_lines = file.read()
    event2 = next(send())
    if event2 == '10':
        n_pkt = 10
    elif event2 == '100':
        n_pkt = 100
    elif event2 == '1000':
        n_pkt = 1000
    else:
        n_pkt = 10000
    # print(n_pkt)
    # print("No_Packets")
    data = line_no[4][10:]
    print(data)
    filedata = list_of_lines.replace(f'n_packets={data}', f'n_packets={n_pkt}\n')
    with open("../1_Exp_Haptic_Data/settings.txt", "w") as file:
        list_of_lines = file.write(filedata)
    # window.close()



def select_packet_MD():
    with open("../2_Exp_Mouse_VREP_Feedback/settings.txt", "r") as file:
        line_no = file.readlines()
    with open("../2_Exp_Mouse_VREP_Feedback/settings.txt", "r") as file:
        list_of_lines = file.read()
    event2 = next(send())
    if event2 == '10':
        n_pkt = 10
    elif event2 == '100':
        n_pkt = 100
    elif event2 == '1000':
        n_pkt = 1000
    else:
        n_pkt = 10000
    # print(n_pkt)
    # print("No_Packets")
    data = line_no[4][10:]
    print(data)
    filedata = list_of_lines.replace(f'n_packets={data}', f'n_packets={n_pkt}\n')
    with open("../2_Exp_Mouse_VREP_Feedback/settings.txt", "w") as file:
        list_of_lines = file.write(filedata)


def graph_plotting_Exp1():
    event01 = next(send())
    print(""+str(event01))
    if event01=='HD-10':
        # print("Open HD-10")
        file = 'HD_10'
    elif event01=='HD-100':
        # print("Open HD-100")
        file = 'HD_100'
    elif event01=='HD-1000':
        # print("Open HD-1000")
        file = 'HD_1000'
    else :
        # print("Open HD-1000")
        file = 'HD_10000'
    file_path='../1_Exp_Haptic_Data/HD_latencyfiles/{}'.format(file)
    ploting.read_latencies_file(file_path)
    save_dir = '../1_Exp_Haptic_Data/HD_graphs'
    ploting.draw_timeseries(ploting.read_latencies_file(file_path),save_dir,file)


def graph_plotting_Exp2():
    event01 = next(send())
    print(""+str(event01))
    if event01=='MD-10':
        # print("Open HD-10")
        file = 'MD_10'
    elif event01=='MD-100':
        # print("Open HD-100")
        file = 'MD_100'
    elif event01=='MD-1000':
        # print("Open HD-1000")
        file = 'MD_1000'
    else :
        # print("Open HD-1000")
        file = 'MD_10000'
    file_path='../2_Exp_Mouse_VREP_Feedback/MD_latencyfiles/{}'.format(file)
    ploting.read_latencies_file(file_path)
    save_dir='../2_Exp_Mouse_VREP_Feedback/MD_graphs'
    ploting.draw_timeseries(ploting.read_latencies_file(file_path),save_dir,file)





# select_packet_n()
# graph_plotting_Exp1()



