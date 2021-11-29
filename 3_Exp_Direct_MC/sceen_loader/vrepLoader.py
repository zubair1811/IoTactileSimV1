import os
# vrep_path_0='/home/zubair/Downloads/0VREP/vrep.sh'
# vrep_path_1='/home/zubair/Downloads/1VREP/coppeliaSim.sh'
vrep_path_2='/home/zubair/Downloads/2VREP/coppeliaSim.sh'
# vrep_scene='./20210915a.ttt'

# vrep_scene='../3_Exp_Direct_MC/sceen_loader/20210915a.ttt'
vrep_scene='../3_Exp_Direct_MC/sceen_loader/Virtual_Model.ttt'
# os.system("sudo "+vrep_path+" -s "+"v-rep/"+vrep_scene)
os.system("sudo "+vrep_path_2+" -s "+vrep_scene)


