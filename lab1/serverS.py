import socket 
import pandas as pd 
import numpy as np 

df = pd.read_csv(r"Foodbill.csv") 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((socket.gethostname(), 1024)) 
s.listen(1) 
list1=[] 

while True: 
    est, addr = s.accept() 
    print(f"Connection established to {addr} ") 
    est.send(bytes("Select you option\nI.Insertion\nM-Modification\nV-View\nU-Update\n", "utf-8")) 
    ch = est.recv(10).decode("utf-8") 
    if ch == 'I': 
        est.send(bytes("Enter Date :", "utf-8")) 
        Date = est.recv(1000).decode("utf-8") 
        est.send(bytes("Enter FoodId : ", "utf-8")) 
        FoodId = est.recv(1000).decode("utf-8") 
        est.send(bytes("Enter Quantity :","utf-8")) 
        Quantity = est.recv(1000).decode("utf-8") 
        Quantity = float(Quantity) 
        est.send(bytes("Enter Cost: ", "utf-8")) 
        Cost = est.recv(1000).decode("utf-8") 
        Cost = float(Cost) 

        list1 = [[Date, FoodId, None, Quantity, Cost, None]] 

        df1 = pd.DataFrame(list1, columns=['Date','FoodId','Category','Quantity','Cost','Totalcost']) 
        df1.to_csv(r'Foodbill.csv',mode='a',index=False,header=False) 
        est.send(bytes("Successfully inserted new food item\n", "utf-8")) 

    elif ch == 'M': 
        df['Totalcost'] = df['Quantity']*df['Cost'] 
        df.to_csv(r"Foodbill.csv", mode='w', index=False) 
        est.send(bytes("Successfully modified all the total costs\n", "utf-8")) 
    elif ch == 'V': 
        est.send(bytes("Foodbill.csv","utf-8")) 
    elif ch == 'U': 
        est.send(bytes("Enter FoodId :", "utf-8")) 
        FoodId = est.recv(1000).decode("utf-8") 
        if FoodId[0] == 'I': 
            df.loc[df['FoodId'] == FoodId,'Category'] = 'Italian' 
        if FoodId[0] == 'D': 
            df.loc[df['FoodId'] == FoodId,'Category'] = 'Dosa' 
        if FoodId[0] == 'A': 
            df.loc[df['FoodId'] == FoodId,'Category'] = 'Apple' 
        if FoodId[0] == 'B': 
            df.loc[df['FoodId'] == FoodId,'Category'] = 'Biryani' 
        df.to_csv(r"Foodbill.csv", mode='w', index=False) 

        est.send(bytes("Successfully updated category of "+FoodId+"\n", "utf-8"))