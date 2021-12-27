# -*- coding: utf-8 -*-

import time
import json

def checkCapacity(contents,knapsack_cap):
    """ contents is expected as a dictionaryof the form {item_id:(volume,value), ...} """
    """ This function returns True if the knapsack is within capacity; False if the knapsack is overloaded """
    load = 0
    if isinstance(contents,dict):
        for this_key in contents.keys():
            load = load + contents[this_key][0]
        if load <= knapsack_cap:
            return True
        else:
            return False
    else:
        print("function checkCapacity() requires a dictionary")

def knapsack_value(items):
    value = 0.0
    if isinstance(items,dict):
        for this_key in items.keys():
            value = value + items[this_key][1]
        return(value)
    else:
        print("function knapsack_value() requires a dictionary")

def getData():
    f = open('C:\\Users\\18046\\CTBA\\BUAD5112Knapsack-master\\knapsack.json','r')
    x = json.load(f)
    f.close()
    for i in range(len(x)):
        myData = x[i]['data']
        x[i]['data'] = {}
        for j in range(len(myData)):
            x[i]['data'][j] = tuple(myData[j]) 
    return x

def load_knapsack(items,knapsack_cap):
       
    
    items_to_pack = []   
    value = 0.0
    load = 0.0            
               
      
    master = [[k,v] for k,v in items.items()]
    master=sorted(master,key=lambda x:x[1],reverse=False)
    
    ID = [item[0] for item in master]
   
    while load < knapsack_cap:
        if load <= knapsack_cap:
            packID = ID[0]
            load += items[packID][0]
            if load <= knapsack_cap:
                items_to_pack.append(packID)
                load += items[packID][0]
                value += items[packID][1]
                
    return items_to_pack
            
                    
    
    
    
    
    
 
    






