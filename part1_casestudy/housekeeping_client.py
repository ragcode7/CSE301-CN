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
        name= input("Name of staff: ")
        date=input("Log for date (dd-mm-yyyy): ")

        print("_________________________________________________________________")

        print("Housekeeping data ")
        floor=int(input("Enter your assigned floor level for the day"))
        count_ra=input("Number of rooms (1,2, executive) cleaned: ")
        count_ma=input("Number of meeting/conference rooms cleaned: ")
        count_st=input("Number of rooms stocked with essentials:  ")
        count_ge=bool(input("Was the general common spaces vacuumed: (TRUE or FALSE) "))
        count_fu=bool(input("Check for functionality of elevators, water coolers on assigned floor: (TRUE or FALSE)  "))
        count_man=int(input("Room which needs manager intervention: "))
        des=str(input("Any personalized/ extras for a guest. Mention room number and the description"))


    
        insert_data={'Name of staff ':name, 'Date':date, 'Floor assigned':floor,'Rooms cleaned':count_ra,'Conference/Meeting rooms cleaned':count_ma,'Room essentials stocked':count_st,'Vaccumed common space':count_ge, 'Check for functionality':count_fu,'Room# for manager intervention':count_man,'Guest personalization':des}
        
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









        
