import json
from collections import defaultdict
def read(path):
    con=json.load(open(path))
    return con
def save(path,con):
    fd = open(path, 'a')
    fd.write(json.dumps(con))
    fd.close()
staticDyn_link_load=read("../Data/staticDyn_link_load.json")
staticDyn_linknumber=read("../Data/staticDyn_linknumber.json")
num_flows=[10000,20000,30000,40000,50000]
for num in num_flows:
    cfd=defaultdict(int)
    for link in staticDyn_link_load[str(num)]:
        if(staticDyn_link_load[str(num)][link]<0.2):
           cfd[0]+=staticDyn_linknumber[str(num)][link]
        elif(staticDyn_link_load[str(num)][link]<0.4):
            cfd[1] += staticDyn_linknumber[str(num)][link]
        elif(staticDyn_link_load[str(num)][link]<0.6):
            cfd[2] += staticDyn_linknumber[str(num)][link]
        elif(staticDyn_link_load[str(num)][link]<0.8):
            cfd[3] += staticDyn_linknumber[str(num)][link]
        else:
            cfd[4] += staticDyn_linknumber[str(num)][link]
    save("cdf_"+str(num)+".json",cfd)

print staticDyn_link_load
print staticDyn_linknumber
