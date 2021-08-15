import socket
import numpy as np
import pandas as pd
import pickle

SERVER=socket.gethostname()
PORT=5001
ADDR=(SERVER,PORT)
CHUNK_SIZE=1024

FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECT"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client.connect(ADDR)
except socket.error as error:
    print(
        "Server seems to be down. Sorry for the inconvience caused. Please try again sometime later" + "\n" + str(error)
    )

cont="Y"

def details():
    print("Details")
    things_to_do=("Enter details (E)", "View Details [V]")

    for x in things_to_do:
        print(x)
    
    choice=input("Enter your choice: ")

    if choice=="E":
        func="Enter".encode('utf-8')
        client.send(func)
        print("_________________________________________________________________")
        print("Enter values to be inserted: ")
        name= input("Name of manager: ")

        print("_________________________________________________________________")

        print("Rooms : 2 & 3 bed , executive rooms ")
        count_sa=input("Available single bed rooms: ")
        count_sr=input("Reserved single bed rooms: ")
        cost_s=float(input("Cost of single bed: "))
        count_ba=input("Available double bed rooms: ")
        count_br=input("Reserved double bed rooms: ")
        cost_d=float(input("Cost of double bed: "))
        count_ea=input("Available executive rooms: ")
        count_er=input("Reserved executive rooms: ")
        cost_e=float(input("Cost of executive room: "))

        print("_________________________________________________________________")

        print("Rooms : Meeting/Conference")
        count_cr=input("Avaialable meeting& conference rooms: ")
        count_rr=input("Reserved meeting & conference rooms: ")
        cost_c=float(input("Cost of meeting/conference room: "))
        print("_________________________________________________________________")

        date=input("Date (dd-mm-yyyy): ")

        insert_data={'Name of manager modifying ':name, 'Available single bed rooms':count_sa , 'Reserved single bed rooms' :count_sr, 'Cost of single bed' :cost_s, 'Available double bed rooms':count_ba , 'Reserved double bed rooms' :count_br, 'Cost of double bed' :cost_d, 'Available executive rooms':count_ea , 'Reserved executive rooms' :count_er, 'Cost of executive' :cost_e,'Available conference room':count_cr , 'Reserved conference room' :count_rr, 'Cost of conference room' :cost_c, 'Date':date}
        msg = pickle.dumps(insert_data)
        msg = bytes(msg)
        status = client.send(msg)
        print("Status of sending: ",status)
    if choice == "V":
        func = "View".encode(FORMAT)
        client.send(func)
       # msg = client.recv(CHUNK_SIZE)
        data = []
        send=True
        while send==True: 
            packet = client.recv(4096)
            if not packet: break
            data.append(packet)
            data_arr = pickle.loads(b"".join(data))
            print (data_arr)
            send=False
       # print(recd)
    else:
        print("Try again, you lack privileges to do more")
    print("Do you want to continue editing? (Y/N)",end=" ")
    cont=input()
def server():
    p = 80
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = socket.gethostbyname('www.google.com')
    print("Google:",host_ip) 
    status = s.connect((host_ip,p))
    print(status, ": Status of connection")
while True and cont=="Y":
    print("INVENTORY MANAGEMENT FOR HOTEL MANAGEMENT SYSTEM")
    print("Choose operation: ")
    options = ["Details (D) ","Check server status (S) "]
    for x in options:
        print(x)
 
    choice = input()
 
    if choice == "D":
        details()
 
    elif choice == "S":
        server()
        break
    else:
        print("try again")
    print("Do you want to continue?(Y/N)",end=" ")
    cont=input()









        
