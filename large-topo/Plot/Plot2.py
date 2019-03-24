#coding=utf-8
import json
import string
import random

import numpy as np
import matplotlib.pyplot as pl

number_of_flow = [20000,40000,60000,80000,100000]
prix="final_"
Controller_name=["staticDyn_controller_load",\
           "Dynmaic_controller_load"]
Link_name=[ "staticDyn_link_load", \
            "Dynamic_link_load", \
            "Static_link_load"]
Response_time=["Dynmaic_response_time",\
               "staticDyn_response_time"]
def file_name(name):
    return "../Data/{0}".format(name)+".json"  #rounding

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 22,
        }

elements1=["ave_edge","ave_objective","ave_switch"]
number=3
ylable=["Controller Load Ratio","Ave Controller Load Ratio","Response Time(x10^3)","Link Load Ratio"]
def getData(name):
    file_path = file_name(name)
    # with open(file_path,'r') as f:
    #     data = f.readlines()
    # f.close()
    datas=json.load(open(file_path))
    return datas
    # if results[0] >= 1.0:
    #     return 1.0
    # else:
    #     return results[0]
x_label = []
for num in number_of_flow:
    x_label.append(getData("deploy_flow_number")[str(num)] / float(1000))
#
results={}
# for contro in Controller_name:
#     data=[]
#     for num in number_of_flow:
#        data.append(getData(prix+contro)[str(num)])
#     results[prix+contro]=data
# for element in Response_time:
#     data=[]
#     for num in number_of_flow:
#        data.append(getData(element)[str(num)]/float(1000))
#     results[element]=data
for link in Link_name:
    data=[]
    for num in number_of_flow:
       data.append(getData(prix+link)[str(num)])
    results[prix+link]=data

print x_label
print results
# for key in results:
#     print key, results[key]

# line_style = {"avg_alg0": "r-s",\
#               "avg_alg1": "g-*",\
#               "avg_alg2": "k-+",\
#               "avg_alg3": "c-p"}
line_style={"ave_staticDyn_controller_load":"r-s", \
            "ave_Dynmaic_controller_load":"g-*", \
            "ave_switch":"k-+"}
line_style2={"Dynmaic_response_time":"r-s", \
            "staticDyn_response_time":"g-*", \
            "ave_switch":"k-+"}
line_style3={"final_staticDyn_link_load":"r-s", \
            "final_Dynamic_link_load":"k-+", \
            "final_Static_link_load": "c-p"}

# line_label = {"avg_alg0": "my_alg",\
#               "avg_alg1": "OSPF",\
#               "avg_alg2": "OSPF_Random",\
#               "avg_alg3": "ECMP"}
line_label1={"ave_staticDyn_controller_load":"Dynamic&Static",\
           "ave_Dynmaic_controller_load":"Dynamic"}
line_label2={"Dynmaic_response_time":"dynmaic_response_time", \
            "staticDyn_response_time":"Dynamic&Static_response_time"}
line_label3={"final_staticDyn_link_load":"Dynamic&Static", \
            "final_Dynamic_link_load":"Dynamic", \
            "final_Static_link_load": "Static"}

for key in results.keys():
    pl.plot(x_label, results[key], line_style3[key], label=line_label3[key])
#pl.plot(x_label,results, line_style[elements[number]],label = line_label[elements[number]])
# pl.plot(number_of_flow,y,'r',label="red line")
pl.ylim(0.0,20.0)


pl.xlabel('Number of Flows(x10^3)',fontdict = font)
pl.ylabel(ylable[number],fontdict = font)

pl.legend(loc="best")

pl.show()