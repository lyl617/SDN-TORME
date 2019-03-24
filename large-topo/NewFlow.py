#coding=utf-8
import cPickle as pickle
import random
import json
from collections import defaultdict
from  graph_for_l2 import DiGraph
CODEC='utf-8'

mynet="200h100r.json"
start_path="hosts.json"

fd=open(start_path,'r')
start_node=json.loads(fd.read())
fd.close()
for i in range(0,len(start_node)):
    start_node[i]=start_node[i].encode(CODEC)
g=DiGraph(mynet)
final_staticDyn_control_load={}
final_staticDyn_linknumber={}
final_Dynamic_control_load={}
final_staticDyn_link_load={}
final_Dynamic_link_load={}
final_Dynamic_linknumber={}
final_static_link_load={}
final_static_linknumber={}
statycDyn_response_time = {}  # 动静态控制器响应时间
Dynamic_response_time={}
def GetNewHosts(num_flow,unum,flow_traffic,big,small,cu,ce,paths):
    alg0=0#控制器负载
    alg1=0#控制器平均负载
    alg2=0#网络负载率
    num_big_flow=num_flow/4
    num_small_flow=num_flow-num_big_flow
    big_flow=big*flow_traffic
    small_flow=small*flow_traffic
    weight=[]
    weight.extend([big_flow for i in range(0,num_big_flow)])
    weight.extend([small_flow for i in range(0,num_small_flow)])
    random.shuffle(weight)
    prefix = "./paper_data2/"
    source_random_file = prefix + "source_random_" + str(num_flow) + ".dat"
    terminal_random_file = prefix + "terminal_random_" + str(num_flow) + ".dat"
    all_edge_alone_file = prefix + "all_edge_alone_" + str(num_flow) + ".dat"
    source_random = pickle.load(open(source_random_file, "rb"))
    terminal_random = pickle.load(open(terminal_random_file, "rb"))
    all_edge_alone = pickle.load(open(all_edge_alone_file, "rb"))
    # print len(all_edge_alone)
    # exit()

    path_file='./Data/paths_'+str(num_flow)+'.json'
    path=json.load(open(path_file))

    #rate=random.randint(30,40)#从已经部署的流表中抽出一部分可能匹配到的
    rate=80
    len1=len(path)#已经部署的流表长度
    len2=len1/100*rate#能匹配到的长度
    flow_table=[]#已部署的流表编号
    flow_table_match=[]#能够匹配到的流表项
    not_match_controller=[]#未能匹配的流上报控制器
    controller_load=defaultdict(int)#动静结合控制器负载
    controller_load_rate={}#控制器负载率
    staticDyn_link_load=defaultdict(int)#动静态链路负载
    staticDyn_link_number = defaultdict(int)  # 动静态链路数目
    statycDyn_link_loadrate={}#动静态链路负载率
    statycDyn_link_numberrate={}#动静态链路数目比例

    for i in path:
        flow_table.append(i.encode('utf-8'))
    random.shuffle(flow_table)
    match_flow=[]

    #动静态
    total_flow_paths=0
    for i in range(len2):#匹配到的流
        #match_number=int(random.choice(flow_table))
        match_number=int(flow_table[i])
        match_flow.append(match_number)
        for link in all_edge_alone[match_number]:
            staticDyn_link_number[link]+=1
            total_flow_paths+=1
            staticDyn_link_load[link]+=weight[i]

    for i in range(num_flow-len2):#新流过来时给匹配不到的流分配控制器
        contro=random.randint(0,unum-1)
        controller_load[contro]+=1
        not_match_controller.append(contro)
        link_random=random.randint(0,num_flow-1)
        while (link_random in match_flow):
              link_random=random.randint(0,num_flow-1)
        # print link_random
        # print all_edge_alone[link_random]
        match_flow.append(link_random)
        for link in all_edge_alone[link_random]:
            staticDyn_link_number[link]+=1
            total_flow_paths += 1
            staticDyn_link_load[link]+=weight[len2+i]
    for link in staticDyn_link_load:
        statycDyn_link_loadrate[link]=staticDyn_link_load[link]/float(ce)
        statycDyn_link_numberrate[link]=staticDyn_link_number[link]/float(total_flow_paths)
    responson_time = []
    for i in range(unum):
        controller_load_rate[i]=controller_load[i]/float(cu)
        time=0
        for j in range(controller_load[i]):
            time+=j*0.02
        responson_time.append(time/float(controller_load[i]))
    statycDyn_response_time[num_flow]=max(responson_time)
    final_staticDyn_control_load[num_flow]=controller_load_rate
    final_staticDyn_link_load[num_flow]=statycDyn_link_loadrate
    final_staticDyn_linknumber[num_flow]=statycDyn_link_numberrate

    #动态
    total_flow_paths = 0
    match_flow2=[]
    random.shuffle(weight)
    controller_load2 = defaultdict(int)  # 动态控制器负载
    controller_load2_rate={}#控制器负载率
    dynamic_link_load = defaultdict(int)  # 动态链路负载
    dynamic_link_loadrate={}#链路负载率
    dynatic_link_number = defaultdict(int)  # 动态链路数目
    dynatic_link_numberrate = {}
    for i in range(num_flow):
        contro = random.randint(0, unum - 1)
        controller_load2[contro] += 1
        match_number2=random.randint(0,num_flow*paths-1)
        while (match_number2 in match_flow2):
            match_number2 = random.randint(0, num_flow * paths - 1)
        match_flow2.append(match_number2)
        for link in all_edge_alone[match_number2]:
            dynamic_link_load[link]+=weight[i]
            dynatic_link_number[link]+=1
            total_flow_paths+=1
    for i in range(unum):
        controller_load2_rate[i]=controller_load2[i]/float(cu)
        time = 0
        for j in range(controller_load2[i]):
            time += j * 0.02
        responson_time.append(time / float(controller_load[i]))
    Dynamic_response_time[num_flow] = max(responson_time)
    for link in dynamic_link_load:
        dynamic_link_loadrate[link]=dynamic_link_load[link]/float(ce)
        dynatic_link_numberrate[link] = dynatic_link_number[link] / float(total_flow_paths)
    final_Dynamic_control_load[num_flow]=controller_load2_rate
    final_Dynamic_link_load[num_flow]=dynamic_link_loadrate
    final_Dynamic_linknumber[num_flow]=dynatic_link_numberrate

    #静态
    total_flow_paths = 0
    random.shuffle(weight)
    static_link_load = defaultdict(int)  # 静态链路负载
    static_link_number = defaultdict(int)  # 静态链路数目
    static_link_loadrate={}
    static_link_numberrate = {}
    for i in range(num_flow):
        match_number3=random.randint(0, num_flow * paths - 1)
        for link in all_edge_alone[match_number3]:
            static_link_load[link]+=weight[i]
            static_link_number[link]+=1
            total_flow_paths+=1
    for link in static_link_load:
       static_link_loadrate[link]=static_link_load[link]/float(ce)
       static_link_numberrate[link]=static_link_number[link]/float(total_flow_paths)
    final_static_link_load[num_flow]=static_link_loadrate
    final_static_linknumber[num_flow]=static_link_numberrate
def GetMax(dicts):
    return max([dicts[dict] for dict in dicts])
def GetAve(dicts):
    return sum([dicts[dict] for dict in dicts])/float(len(dicts))

def save(path, con):
    fd = open(path, 'a')
    fd.write(json.dumps(con))
    fd.close()

num_flows=[60000]
ce=1000
cu=18000
unum=5
big=0.5
small=0.03
for num in num_flows:
    GetNewHosts(num,unum,flow_traffic=1,big=big,small=small,cu=cu,ce=ce,paths=3)
save('./Data/staticDyn_response_time.json',statycDyn_response_time)
save('./Data/Dynmaic_response_time.json',Dynamic_response_time)

save('./Data/staticDyn_controller_load.json',final_staticDyn_control_load)
save('./Data/staticDyn_link_load.json',final_staticDyn_link_load)
save('./Data/staticDyn_linknumber.json',final_staticDyn_linknumber)

save('./Data/Dynmaic_controller_load.json',final_Dynamic_control_load)
save('./Data/Dynamic_link_load.json',final_Dynamic_link_load)
save('./Data/Dynamic_linknumber.json',final_Dynamic_linknumber)

save('./Data/Static_link_load.json',final_static_link_load)
save('./Data/Static_linknumber.json',final_static_linknumber)



