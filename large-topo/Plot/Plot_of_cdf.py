#coding=utf-8
import json
import string
import random
import numpy as np
import matplotlib.pyplot as pl

number_of_flow = [20000,40000,60000,80000,100000]
prix="cdf_"
def file_name(name):
    return "{0}".format(name)+".json"  #rounding

font = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 22,
        }

elements1=["ave_edge","ave_objective","ave_switch"]
number=0
ylable=["Ratio"]
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

#
results={}
x_label ={}
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
for num in number_of_flow:
    datas=getData(prix+str(num))
    ylabe=[]
    xlabe=[]
    for (k,v) in datas.items() :
       xlabe.append(int(k))
    xlabe.sort()
    for i in xlabe:
         ylabe.append(datas[str(i)])
    results[prix+str(num)]=ylabe
    x_label[prix+str(num)]=xlabe
print results
print x_label





# for key in results:
#     print key, results[key]

line_style = {"cdf_20000": "r-s",\
              "cdf_40000": "g-*",\
              "cdf_60000": "k-+",\
              "cdf_80000": "c-p",\
              "cdf_100000":"b-*"}

line_label = {"cdf_20000": "Flow number:10000",\
              "cdf_40000": "Flow number:20000",\
              "cdf_60000": "Flow number:60000",\
              "cdf_80000": "Flow number:80000",\
              "cdf_100000":"Flow number:100000"}


for key in results.keys():
    pl.plot(x_label[key], results[key], line_style[key], label=line_label[key])
#pl.plot(x_label,results, line_style[elements[number]],label = line_label[elements[number]])
# pl.plot(number_of_flow,y,'r',label="red line")
pl.ylim(0.0,2.0)


pl.xlabel('Ratio',fontdict = font)
pl.ylabel(ylable[number],fontdict = font)

pl.legend(loc="best")

pl.show()