#coding=utf-8
import json
import string
import random

import numpy as np
import matplotlib.pyplot as pl

number_of_flow = [20000,40000,60000,80000,100000]

def file_name(name):
    return "../Data/{0}".format(name)+".json"  #rounding

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 22,
        }

elements1=["ave_edge","ave_objective","ave_switch"]
number=2
ylable=['Link Load Ratio','Resource cost','Switch Load Ratio']
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

#
#
# for alg in range(0,4):
#     prefix = "avg_alg"+str(alg)
#
#     results[prefix] = []
#
#     for number in number_of_flow:
#         results[prefix].append(getData(prefix,number))
#first three plot
results = []
for num in number_of_flow:
    x_label.append(getData("deploy_flow_number")[str(num)]/float(1000))
    results.append(getData(elements1[number])[str(num)])

print x_label
print results


# for key in results:
#     print key, results[key]

# line_style = {"avg_alg0": "r-s",\
#               "avg_alg1": "g-*",\
#               "avg_alg2": "k-+",\
#               "avg_alg3": "c-p"}
line_style={"ave_edge":"r-s", \
            "ave_objective":"g-*", \
            "ave_switch":"k-+"}

# line_label = {"avg_alg0": "my_alg",\
#               "avg_alg1": "OSPF",\
#               "avg_alg2": "OSPF_Random",\
#               "avg_alg3": "ECMP"}
line_label1={"ave_edge":"Link_load",\
            "ave_objective":" Resource cost of the data plane",\
            "ave_switch":"Switch_load"}



pl.plot(x_label, results, line_style[elements1[number]], label=line_label1[elements1[number]])
#pl.plot(x_label,results, line_style[elements[number]],label = line_label[elements[number]])
# pl.plot(number_of_flow,y,'r',label="red line")
pl.ylim(0.0,3.0)

pl.xlabel('Number of Flows(x10^3)',fontdict = font)
pl.ylabel(ylable[number],fontdict = font)

pl.legend(loc="best")

pl.show()