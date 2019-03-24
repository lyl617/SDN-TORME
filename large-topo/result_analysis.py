#coding=utf-8
import json
import cPickle as pickle
from collections import defaultdict

all_objective={}
all_edge={}
all_switch={}
paths=defaultdict(lambda :(defaultdict(int)))
def save(path,con):
    fd = open(path, 'a')
    fd.write(json.dumps(con))
    fd.close()

def avg(num_flow,nums):
    prefix = "./paper_result/"
    objective_file=prefix+"objective_"+str(num_flow)+".json"
    edge_file =prefix+ "edge_" + str(num_flow) + ".json"
    switch_file = prefix+"switch_" + str(num_flow) + ".json"
    choosepath_file = prefix+"choosepath_" + str(num_flow) + ".json"
    all_node_alone_file = "./paper_data2/all_node_alone_" + str(num_flow) + ".dat"
    all_node_alone = pickle.load(open(all_node_alone_file, "rb"))


    sum_obje=0
    sum_edge=0
    sum_switch=0
    objective=json.load(open(objective_file))
    edge = json.load(open(edge_file))
    switch = json.load(open(switch_file))
    choosepath = json.load(open(choosepath_file))
    path1=choosepath["0"]

    for i,pathnum in enumerate(path1):
        if pathnum!=4:
            paths[num_flow][i]=all_node_alone[i*3+path1[i]]

    for i in range(nums):
        nu=str(i)
        sum_obje+=objective[nu]
        sum_edge+=edge[nu]
        sum_switch+=switch[nu]
    ave_obje=sum_obje/nums
    ave_edge=sum_edge/nums
    ave_switch=sum_switch/nums
    all_objective[num_flow]=ave_obje
    all_edge[num_flow]=ave_edge
    all_switch[num_flow]=ave_switch
    #print all_objective
num_flows=[60000]
nums=3
for num in num_flows:
    avg(num,nums)
for num in num_flows:
    save('./Data/paths_'+str(num)+'.json', paths[num])
save('./Data/ave_objective.json',all_objective)
save('./Data/ave_edge.json',all_edge)
save('./Data/ave_switch.json',all_switch)
print "end"





