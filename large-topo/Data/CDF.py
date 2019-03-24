import json
from collections import defaultdict
def read(path):
    con=json.load(open(path))
    return con
dict_of_load=defaultdict(int)
staticDyn_link_load=read("staticDyn_link_load.json")
staticDyn_linknumber=read("staticDyn_linknumber.json")
numberrate=0
for link in staticDyn_link_load["800"]:
    linkload=staticDyn_link_load["800"][link]
    linknumberrate=staticDyn_linknumber["800"][link]
    numberrate+=linknumberrate
    dict_of_load[linkload]+=linknumberrate
x=[]
y=[]
for (k,v) in dict_of_load.items():
    x.append(k)
x.sort()
for i in x:
    y.append(dict_of_load[i])
sum=0
final_y=[]
for i in range(len(y)):
     sum+=y[i]
     final_y.append(sum)
fd=open("cdf.txt",'a')
for i in range(len(x)):
    fd.write(str(x[i])+' '+str(final_y[i])+'\n')
fd.close()
print final_y
#print staticDyn_linknumber["20000"]