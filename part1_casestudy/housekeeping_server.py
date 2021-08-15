import datetime
import socket
import threading
import numpy as np
import pandas as pd
import pickle

SERVER=socket.gethostname()
PORT=5001
ADDR =(SERVER,PORT)
CHUNK_SIZE='utf-8'
DISCONNECT_MESSAGE="DISCONNECT"

items=pd.read_csv("./housekeeping.csv")

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print('Server starting up')
print('Server address:', ADDR)

def Log(inp):
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    print("[",current_time,"]Operation",inp,"has been initiated")

while True:
    Items=pd.read_csv("./housekeeping.csv")
    client,addr=server.accept()
    print(f'New connection established with',(addr))
    inp=(client.recv(CHUNK_SIZE).decode('utf-8'))
    if(inp=="Enter"):
        #Log(inp)
        data=client.recv
        recd=pickle.loads(data)
        print("Values received: ")
        print(recd)
        Items=Items.append(recd,ignore_index=True)

    elif(inp=="View"):
        print(Items)
        #Log(inp)
        send_file=pickle.dumps(Items)
        stat=client.send(send_file)
        print(stat)
        
