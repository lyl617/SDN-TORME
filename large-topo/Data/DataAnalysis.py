import json
def read(path):
    con=json.load(open(path))
    return con
def save(path,con):
    fd = open(path, 'a')
    fd.write(json.dumps(con))
    fd.close()
def GetMax(dicts):
    return max([dicts[dict] for dict in dicts])
def GetAve(dicts):
    return sum([dicts[dict] for dict in dicts])/float(len(dicts))
file_name=["staticDyn_controller_load",\
           "staticDyn_link_load",\
           "Dynmaic_controller_load",\
           "Dynamic_link_load",\
           "Static_link_load"]
num_flows=[60000]
cus=18000
for file in file_name:
    result={}
    con=read(file+".json")
    for num in num_flows:
        result[num]=GetMax(con[str(num)])
    save("Max_"+file+".json",result)
    print result
