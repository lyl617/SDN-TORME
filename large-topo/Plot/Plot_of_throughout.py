import numpy as np
import matplotlib.pyplot as pl
import json
Throuthout_name=[ "staticDyn_Throuthout", \
            "Dynamic_Throuthout", \
            "Static_Throuthout"]
font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 22,
        }
num_flows=[20000,40000,60000,80000,100000]
ylable=["Throughout Ratio"]
number=0
def file_name(name):
    return "../Data/{0}".format(name)+".json"  #rounding
def getData(name):
    file_path = file_name(name)
    # with open(file_path,'r') as f:
    #     data = f.readlines()
    # f.close()
    datas=json.load(open(file_path))
    return datas
x_label = []
for num in num_flows:
    x_label.append(getData("deploy_flow_number")[str(num)] / float(1000))
results=json.load(open("Throughput.json"))

line_style={"staticDyn_Throuthout":"r-s", \
            "Dynamic_Throuthout":"g-*", \
            "Static_Throuthout":"k-+"}
line_label={"staticDyn_Throuthout":"Dynamic&Static", \
            "Dynamic_Throuthout":"Dynamic", \
            "Static_Throuthout": "Static"}
for key in results.keys():
    pl.plot(x_label, results[key], line_style[key], label=line_label[key])
#pl.plot(x_label,results, line_style[elements[number]],label = line_label[elements[number]])
# pl.plot(number_of_flow,y,'r',label="red line")
pl.ylim(0.0,100.0)


pl.xlabel('Number of Flows(x10^3)',fontdict = font)
pl.ylabel(ylable[number],fontdict = font)

pl.legend(loc="best")

pl.show()
