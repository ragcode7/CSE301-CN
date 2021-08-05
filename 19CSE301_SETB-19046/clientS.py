import socket 
import pandas as pd 
import numpy as np 

df = pd.read_csv(r"Foodbill.csv") 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((socket.gethostname(), 1024)) 
ch = input(s.recv(1000).decode("utf-8")) 
s.send(ch.encode("utf-8")) 

if ch == 'I': 
    date = input(s.recv(1000).decode("utf-8")) 
    s.send(date.encode("utf-8")) 
    FoodId = input(s.recv(1000).decode("utf-8")) 
    s.send(FoodId.encode("utf-8")) 
    Quantity = float(input(s.recv(1000).decode("utf-8"))) 
    s.send(str(Quantity).encode("utf-8")) 
    Cost = float(input(s.recv(1000).decode("utf-8"))) 
    s.send(str(Cost).encode("utf-8")) 
    print(s.recv(5000).decode("utf-8")) 
elif ch == 'M': 
    print(s.recv(5000).decode("utf-8")) 
elif ch == 'V': 
    print(pd.read_csv(s.recv(5000).decode("utf-8"))) 
elif ch == 'U': 
    FoodId = input(s.recv(1000).decode("utf-8")) 
    s.send(FoodId.encode("utf-8")) 
    print(s.recv(5000).decode("utf-8"))