# IoTactileSim: A Virtual Testbed for Tactile Industrial Internet of Things Services  
A virtual Tesebed Framework for Tactile Industrial IoTs to investiage the QoS and QoE requirments and test their proposed Algorithms.
## Package and OS Requirments 
* Ubuntu 18.04 LTS
* Python v3.8
* [Mininet Emulator 3.6.9](http://mininet.org/download/)
* [CoppeliaSim 4.2](https://www.coppeliarobotics.com/)
* Other packeges 
(pynput==1.1.7; ;pandas; Sim_GUI; socklet; pickle; multiprocessing;  libgl1-mesa-dev; mss==3.1.2; numpy; matplotlib)
#### How to install
1- Go to mininet website [mininet](https://mininet.org/download/)
```
git clone https://github.com/mininet/mininet
cd mininet
git tag  # list available versions
git checkout -b mininet-2.3.0 2.3.0  # or whatever version you wish to install
cd ..
PYTHON=python3 util/install.sh -a : install with pyuthon3 version 
```
2- sudo apt-get install python3.8
3- sudo apt install Python3-pip
5- Create alias for python3.8 and pip3 as `python=python3.8, pip=pip3`
4- pip install PySimpleGUI==4.59.0
3- 

## Starting ***IoTactileSim***
*To run the IoTactileSim, go to the folder [Mininet_Emulator](Mininet_Emulator) and run the command $sudo python3 [MininetEmulator.py](Mininet_Emulator/MininetEmulator.py)
* GUI window will poop up to selecte start simulation tap *(After pressing  start simulation buttion it create netrwork topology and asked for Experiment Type)* ![IoTactileSim](Interface_img/1.png)
1. Exp#1; Haptic Data Transfer
2. Exp#2 Direct Control
3. Exp#3 Mouse Control with Feedback
4. Exit Mininet
* After select desir Experment number it leads towards packet selection module ![IoTactileSim Packet Selection](Interface_img/2.png)
* Select packet number it start the simmulation and store the results into selected Experment latencyfile folder [HD_Latencyfiles](1_Exp_Haptic_Data/HD_latencyfiles/), [MD_Latencyfiles](2_Exp_Mouse_VREP_Feedback/MD_latencyfiles/)
* After finish experiments its open a new window to display results and store in to [HD_graphs](1_Exp_Haptic_Data/HD_graphs/), [MD_graphs](2_Exp_Mouse_VREP_Feedback/MD_graphs/)
* Finaly, ***IoTactileSim*** asked to proceed with new experiment or end simulation.

### Note
The experiment results represent in the paper are stored in Experiment Results Files folder.

## Publication
### If you use this source code, please cite this paper.
[IoTactileSim: A Virtual Testbed for Tactile Industrial Internet of Things Services](https://www.mdpi.com/1424-8220/21/24/8363)

[
@article{zubair2021iotactilesim,
  title={IoTactileSim: A Virtual Testbed for Tactile Industrial Internet of Things Services},
  author={Zubair Islam, Muhammad and Ali, Rashid and Haider, Amir and Kim, Hyungseok},
  journal={Sensors},
  volume={21},
  number={24},
  pages={8363},
  year={2021},
  publisher={MDPI}
}
]


