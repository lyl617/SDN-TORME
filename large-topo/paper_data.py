#coding=utf-8
from pulp import *;
from algorithms import  dijkstra;
from  algorithms import dijkstra2;
from  algorithms import dijkstra3;
from  graph_for_l2 import DiGraph
from collections import defaultdict
import json
import  random
import pickle as pickle

#import cPickle as pickle

CODEC='utf-8'

mynet="fat_tree.json"
start_path="fat_tree_host.json"

fd=open(start_path,'r')
start_node=json.loads(fd.read())
fd.close()
for i in range(0,len(start_node)):
    start_node[i]=start_node[i].encode(CODEC)
g=DiGraph(mynet)
def len_main_path(node,display=0):
    if(display):
        if(len(node)==4):
            print('len is 4',node)

def toInt(node):
    tmp=node[1:]
    return int(tmp)

def gen_data(number_of_flow,net,start_node):
    all_node=[]#所有节点 []
    all_node_alone=[]#每个路径的所有节点 [[][]]
    all_edge=[]#所有边 []
    all_edge_alone=[]#每个路径的所有边 [[][]]

    source=[]
    terminal=[]

    source_random=[]
    terminal_random=[]
    one_edge=[]
    one_node=[]

    source_tmp=[]
    source_number=len(start_node)

    for i in range(0,source_number-1):
        source_tmp.extend([i for jj in range(0,source_number-1-i)])
    #0...0  1...1 2...2
    terminal_tmp=[]
    for i in range(0,source_number-1):
        terminal_tmp.extend(range(source_number-1,i,-1))
    #128...1 128...2 128...3
    random.shuffle(source_tmp)
    random.shuffle(terminal_tmp)
    # print source_tmp
    # print terminal_tmp
    # exit()
    count=0
    source_random=[]
    terminal_random=[]
    while count<number_of_flow:
        s=random.choice(source_tmp)
        d=random.choice(terminal_tmp)
        while s==d:
            s=random.choice(source_tmp)
            d=random.choice(terminal_tmp)
        source_random.append(s)#源节点的索引
        terminal_random.append(d)#目的节点的索引
        count+=1
    source=[start_node[source_random[i]] for i in range(0,len(source_random))]#6000
    terminal=[start_node[terminal_random[i]] for i in range(0,len(terminal_random))]#6000
    number_of_bigflow=len(source_random)/4
    number_of_smallflow=len(source_random)-number_of_bigflow

    for sr in range(0,len(source_random)):
        main_path_all=[]
        one_source_edge=[]
        one_source_node=[]
        path=dijkstra(g,source[sr],terminal[sr])
        main_path=path.get('path')
        #每条流的路径
        for i in range(0,len(main_path)):
            main_path[i]=main_path[i].encode(CODEC)
            main_path_all.append(main_path[i])
        for f in range(0,len(main_path)-3):
            switch1=toInt(main_path[f+1])
            switch2=toInt(main_path[f+2])
            if switch1<switch2:
                one_edge=main_path[f+1]+main_path[f+2]
            else:
                one_edge=main_path[f+2]+main_path[f+1]
            if one_edge not in all_edge:
                all_edge.append(one_edge)
            one_source_edge.append(one_edge)
        all_edge_alone.append(one_source_edge)

        for f in range(0,len(main_path)-2):
            one_node=main_path[f+1]
            if one_node not in all_node:
                all_node.append(one_node)
            one_source_node.append(one_node)
        all_node_alone.append(one_source_node)

        #path2
        one_source_edge = []
        one_source_node = []
        path = dijkstra2(g, source[sr], terminal[sr],main_path_all)
        main_path = path.get('path')
        # 每条流的路径
        for i in range(0, len(main_path)):
            main_path[i] = main_path[i].encode(CODEC)
            main_path_all.append(main_path[i])
        for f in range(0, len(main_path) - 3):
            switch1 = toInt(main_path[f + 1])
            switch2 = toInt(main_path[f + 2])
            if switch1 < switch2:
                one_edge = main_path[f + 1] + main_path[f + 2]
            else:
                one_edge = main_path[f + 2] + main_path[f + 1]
            if one_edge not in all_edge:
                all_edge.append(one_edge)
            one_source_edge.append(one_edge)
        all_edge_alone.append(one_source_edge)
        for f in range(0, len(main_path) - 2):
            one_node = main_path[f + 1]
            if one_node not in all_node:
                all_node.append(one_node)
            one_source_node.append(one_node)
        all_node_alone.append(one_source_node)

        #path3
        one_source_edge = []
        one_source_node = []
        path = dijkstra3(g, source[sr], terminal[sr],main_path_all)
        main_path = path.get('path')
        # 每条流的路径
        for i in range(0, len(main_path)):
            main_path[i] = main_path[i].encode(CODEC)
            main_path_all.append(main_path[i])
        for f in range(0, len(main_path) - 3):
            switch1 = toInt(main_path[f + 1])
            switch2 = toInt(main_path[f + 2])
            if switch1 < switch2:
                one_edge = main_path[f + 1] + main_path[f + 2]
            else:
                one_edge = main_path[f + 2] + main_path[f + 1]
            if one_edge not in all_edge:
                all_edge.append(one_edge)
            one_source_edge.append(one_edge)
        all_edge_alone.append(one_source_edge)

        #print all_edge_alone
        for f in range(0, len(main_path) - 2):
            one_node = main_path[f + 1]
            if one_node not in all_node:
                all_node.append(one_node)
            one_source_node.append(one_node)
        all_node_alone.append(one_source_node)
    #print all_node_alone
        # print main_path_all
        # print all_edge
        # print all_node
    #all_node 所有出现的节点 all_edge 所有出现的边 all_node_alone 一个list中为一条路径中出现的节点 all_edge_alone 一个list中为一条路径中出现的边
    pickle.dump(all_node_alone,open("./paper_data2/all_node_alone"+"_"+str(number_of_flow)+".dat","wb"),True)
    pickle.dump(all_edge_alone, open("./paper_data2/all_edge_alone" + "_" + str(number_of_flow) + ".dat", "wb"), True)
    pickle.dump(source_random, open("./paper_data2/source_random" + "_" + str(number_of_flow) + ".dat", "wb"), True)
    pickle.dump(terminal_random, open("./paper_data2/terminal_random" + "_" + str(number_of_flow) + ".dat", "wb"), True)
    pickle.dump(all_node, open("./paper_data2/all_node" + "_" + str(number_of_flow) + ".dat", "wb"), True)
    pickle.dump(all_edge, open("./paper_data2/all_edge" + "_" + str(number_of_flow) + ".dat", "wb"), True)


if __name__=='__main__':
    flow_number=[6000]
    for num in flow_number:
        gen_data(num,g,start_node)
    print("end")