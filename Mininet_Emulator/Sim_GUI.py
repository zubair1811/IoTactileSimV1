import PySimpleGUI as sg
import PIL.Image

# sg.theme('THEME_winnative')
sg.theme('DefaultNoMoreNagging')
# #---------------- Windiw layout----
# layout=[
#       [sg.Text('Wellcome to Teleopertion Virtaul Testbed', size=(100,1), justification='center',
#                background_color='light blue',text_color='red',font='10')],
#       [sg.Input()],
#       [sg.Button('Button')]
#
# ]
# window=sg.Window(title="Tactile Teleoperation Testbed", layout=layout, size=(400,400),location=(700,200))
# event, value=window.read()
# window.close()
# input("Enter \n"
#       "1 for Haptic Data Experiment\n"
#       "2 for Mouse Experiment\n")

# layout1=[
#
#       [sg.Text('1. '), sg.In(key=1)],
#       [sg.Text('2. '), sg.In(key=2)],
#       [sg.Text('3. '), sg.In(key=3)],
#       [sg.Text('4. '), sg.In(key=4)],
#       [sg.Text('5. '), sg.In(key=5)],
#       [sg.Button('Save'),sg.Button('Exit')]
#
# ]

Frame_layout=[
      [sg.Text('Start Network Simulation'), sg.Button('Start Simulation',button_color=('white','green')),],
      [sg.Button('EXP#1(Haptic Data)'),sg.Button('EXP#2(Direct Control)')],
      [sg.Button('EXP#3(Haptic Driven Teleopertion)')],
      [sg.Button('Display Result'),sg.Button('Exit Mininet')]
]
mainlayput=[
      [sg.Text('Wellcome to Tactile Industrial IoT Testbed', size=(90, 1), justification='center',
               background_color='light blue', text_color='red', font='10')],
      [sg.Frame('Experiment Selection', Frame_layout, font='Any 12', title_color='blue',element_justification='center')],
      # [sg.Image(r'./Sejong.png')]
]
# layout2=[
#       [sg.Text('Wellcome to Teleopertion Virtaul Testbed', size=(100, 1), justification='center',
#                background_color='light blue', text_color='red', font=('Helvetica',12))],
#       [sg.Text('Exp No. 1',justification='center'),sg.Button('Press 1')],
#       [sg.Text('Exp No. 1'),sg.Button('Press 2')],
#       [sg.Text('Exp No. 1'),sg.Button('Press 3')],
#       [sg.Text('Exp No. 1'),sg.Button('Press 4')],
#       [sg.Button('Run'),sg.Button('Exit')]
# ]

window = sg.Window(title="IoTactileSim Testbed", layout=mainlayput, size=(400, 250),
                         location=(700, 200),
                         font=('Helvetica', 12))
def send():
    while True:
        event, values = window.Read()
        yield event
    window.close()






# event1=next(send())
# if event1 == 'Start Simulation':
#       print("Start")
# event2=next(send())
# if event2 == 'Press 1':
#       print("OKay 1")

def select_packet_n():
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
    print(n_pkt)
    # print("No_Packets")
    data = line_no[4][10:]
    print(data)
    filedata = list_of_lines.replace(f'n_packets={data}', f'n_packets={n_pkt}\n')
    with open("../1_Exp_Haptic_Data/settings.txt", "w") as file:
        list_of_lines = file.write(filedata)




# select_packet_n()