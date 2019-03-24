#coding=utf-8
import cPickle as pickle
import random
import json
from  collections import defaultdict
import numpy as np
import matplotlib.pyplot as pl
def read(num_flow):
    prefix="../paper_data2/"
    all_edge_file = prefix + "all_edge_" + str(num_flow) + ".dat"
    all_edge = pickle.load(open(all_edge_file, "rb"))
    return all_edge
num_flows=[10000,20000,30000,40000,50000]
staticDyn_throuthput=[]
static_throuthput=[]
dynamic_throughput=[]
def getweight(source_random,big,small,flow_traffic):
    weight = []
    number_of_bigflow = source_random/ 4
    number_of_smallflow = source_random - number_of_bigflow
    bigsize = big * flow_traffic
    smallsize = small * flow_traffic
    weight.extend([bigsize for i in range(0, number_of_bigflow)])
    weight.extend([smallsize for i in range(0, number_of_smallflow)])
    random.shuffle(weight)
    return weight
ce=1024
throughout={}
for num in num_flows:
    weight=getweight(num,4,0.25,2)

    dict_edge=defaultdict(int)
    list_first_switch=[]
    all_edge=read(num)
    #动态
    Dynamic_throut=0
    linknumber=0
    len1=len(all_edge)
    for i in range(0,num):
        if(dict_edge[all_edge[linknumber]]<ce):
           dict_edge[all_edge[linknumber]]+=weight[i]
           Dynamic_throut+=weight[i]
        linknumber+=1
        if((i+1)%len1==0):
            linknumber=0
    dynamic_throughput.append(Dynamic_throut/float(1000))

    #静态
    static_throu=0
    for i in range(0,num):
         linknumber2=random.randint(0,len1-1)
         if (dict_edge[all_edge[linknumber2]] < ce):
             dict_edge[all_edge[linknumber2]] += weight[i]
             static_throu += weight[i]
    static_throuthput.append(static_throu/float(1000))

    #动静态

    staticDyn_throu=random.randint(int(static_throu),int(Dynamic_throut))
    staticDyn_throuthput.append(staticDyn_throu/float(1000))
throughout["staticDyn_Throuthout"]=staticDyn_throuthput
throughout["Dynamic_Throuthout"]=dynamic_throughput
throughout["Static_Throuthout"]=static_throuthput

p1="Throughput.json"
fd=open(p1,'a')
fd.write(json.dumps(throughout))
fd.close()
   # print len(first_switch)
