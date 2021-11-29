Experiment Number 2b
Simulation setup:
steps:
1- Run mininet topology with hTEM, hTES, hServer, s1, s2,s3 (3 switches, 3 hosts; with  0delay, 1000Mbits)
#links details are below
hTEM-eth0<->s1-eth1 (OK OK)
hServer-eth0<->s2-eth1 (OK OK)
hTES-eth0<->s3-eth1 (OK OK)
s1-eth2<->s2-eth2 (OK OK)
s1-eth3<->s3-eth2 (OK OK)
#net
s1 lo:  s1-eth1:hTEM-eth0 s1-eth2:s2-eth2 s1-eth3:s3-eth2
s3 lo:  s3-eth1:hTES-eth0 s3-eth2:s1-eth3
s2 lo:  s2-eth1:hServer-eth0 s2-eth2:s1-eth2

2- run command on mininet terminal:  xterm hTEM hServer hTES (Create three terminals)
3- Run srv.py at terminal hTES (Go to Exp2b directroy run command; sudo python3 srv.py)
4- Run t1.py at terminal hServer (Go to Exp1 directroy run command; sudo python3 t1.py)


# Findings
send packets ; 10,100, 1000
latency under 0.2 ms

Create latency Files in Result Folder:
N10,N100, N1000

To create Graphs go to Result folder run (sudo python3 latency_measurement_graphs.py <fileNeme: N10>)

