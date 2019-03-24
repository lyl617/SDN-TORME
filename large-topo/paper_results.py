#coding=utf-8
from pulp import *;
from algorithms import  dijkstra;
from  algorithms import dijkstra2;
from  algorithms import dijkstra3;
from  graph_for_l2 import DiGraph
#from GenVC import gen
from collections import defaultdict
import json
import  random
import cPickle as pickle
import sys

if len(sys.argv)<2:
    run_level="INFO"
else:
    run_level="DEBUG"

run_level="DEBUG"

steps=2
flow_number={}#部署流数

def flatten(lists,src):
    for i in lists:
       if type(i)==type([]):
           flatten(i,src)
           continue
       src.append(i)

def my_printer(string,*args):
    print string,":",
    for arg in args:
        print arg," ",
    print " "

def my_loger(level,string,*args):
    if run_level=="DEBUG":
        my_printer(string,args)
    elif run_level=="INFO":
        if level=="DEBUG":
            return
        my_printer(string,args)
    else:
        return
def save(path, con):
    fd = open(path, 'a')
    fd.write(json.dumps(con))
    fd.close()
def action(num_flow,paths,flow_traffic,repeat_time,ce,cu,unum,big,small,entries,d):
    prefix="./paper_data2/"
    all_node_alone=[]
    all_edge_alone=[]
    source_random=[]
    all_node=[]
    all_edge=[]
    all_node_alone_file=prefix+"all_node_alone_"+str(num_flow)+".dat"
    all_edge_alone_file = prefix + "all_edge_alone_" + str(num_flow) + ".dat"
    source_random_file = prefix + "source_random_" + str(num_flow) + ".dat"
    all_node_file = prefix + "all_node_" + str(num_flow) + ".dat"
    all_edge_file = prefix + "all_edge_" + str(num_flow) + ".dat"

    all_node_alone=pickle.load(open(all_node_alone_file,"rb"))
    all_edge_alone=pickle.load(open(all_edge_alone_file,"rb"))
    source_random=pickle.load(open(source_random_file,"rb"))
    all_node=pickle.load(open(all_node_file,"rb"))
    all_edge=pickle.load(open(all_edge_file,"rb"))

    number_of_bigflow=len(source_random)/4
    number_of_smallflow=len(source_random)-number_of_bigflow
    m = defaultdict(lambda :defaultdict(int))
    # p1='VC.json'
    # m=json.load(open(p1))
    # print m['v0']['C2']


    for i in range(len(all_node)):
       unumber=random.randint(0,unum)
       uname="C"+str(unumber)
       m[all_node[i]][uname]=1#节点和哪一个控制器相连

    p1='./Data/VC_'+str(num_flow)+'.json'

    fd=open(p1,'a')
    fd.write(json.dumps(m))
    fd.close()

    # print m['v0']['C1']
    # exit()
    # print all_node_alone[6][0]
    #exit()

    objective={}#数据层性能
    alg0={}#链路负载
    alg1={}#交换机负载
    alg2={}#所选路径
    alg3=0

    for random_time in range(0,repeat_time):
        print "flow traffic and rand time",flow_traffic,random_time
        weight=[]
        num_of_flow=[]
        bigsize=big*flow_traffic
        smallsize=small*flow_traffic
        weight.extend([bigsize for i in range(0,number_of_bigflow)])
        weight.extend([smallsize for i in range(0,number_of_smallflow)])
        num_of_flow.extend(random.randint(80,120) for i in range(0,num_flow))

        random.shuffle(weight)




        for alg in range(0,4):
            if alg==0:
                x_e=defaultdict(lambda :(defaultdict(int)))
                x_v=defaultdict(lambda :(defaultdict(int)))
                x=[[0 for col in range(4)]for row in range(len(source_random))]
                z=[]
                temp=[]
                for i in range(0,len(source_random)):
                    z.append("z"+str(i))
                    for j in range(0,3):
                        x[i][j]="x"+str(i*10+j+1000000)[1:]
                        x[i][3]="z"+str(i)


                flatten(x,temp)

                prob=LpProblem('lptest',LpMinimize)
                e=LpVariable('edge',lowBound=0)
                t=LpVariable('switch',lowBound=0)
                xx=LpVariable.dicts("",temp,lowBound=0,upBound=1)
                #zz=LpVariable.dicts("",z,lowBound=0,upBound=1)

                prob+=0.1*e+0.9*t
                for i in range(0,len(source_random)):#4000
                    prob+=lpSum([xx[j] for j in x[i]])==1
                for i in range(0,len(all_edge_alone)):#12000
                    for edge in all_edge_alone[i]:
                        x_e[edge][x[i/paths][i%paths]]=weight[i/paths]#一条链路在哪条路径上 以及对应的流的大小

                # print len(all_edge)

                for i in all_edge:
                    prob+=lpSum(x_e[i][flow]*xx[flow] for flow in x_e[i]) <= ce*e # 链路负载

                for i,node_alone_ep in enumerate(all_node_alone):#all_node_alone  flow*3
                    #print node_alone_ep
                    # if weight[i/3]==bigsize:
                    #   for node in node_alone_ep[::steps+1]:
                    #      x_v[node][x[i/3][i%3]]=1
                    # else:
                    #      for node in node_alone_ep:
                    #         x_v[node][x[i / 3][i % 3]] = 1
                    for node in node_alone_ep:
                        x_v[node][x[i/paths][i%paths]]=1
                         #print node
                for node in all_node:
                    prob+=lpSum(x_v[node][flow]*xx[flow] for flow in x_v[node])<=entries*t

                for j in range(0, unum):
                    prob+=lpSum(m[all_node_alone[i*paths][0]]['C%s'%j]*xx[zz]*num_of_flow[i] for i,zz in enumerate(z) )<=cu*d




                prob.solve()
                #GLPK().solve(prob)

                # for v in prob.variables():
                #    print v.name,"=",v.varValue
                # print prob.variables()[-2].name,":",prob.variables()[-2].varValue
                # print prob.variables()[-1].name,":",prob.variables()[-1].varValue
                print 'objective_sr=',value(prob.objective)
                alg0[random_time]=prob.variables()[-2].varValue#edge
                alg1[random_time]=prob.variables()[-1].varValue#switch
                objective[random_time]=value(prob.objective)





                #objective+=float(value(prob.objective))
                     #exit()
                # begin=len(prob.variables()[:-1])-len(x)*len(x[0])
                #xp每条流的选择路径
                xp = [[0 for col in range(3)] for row in range(len(source_random))]
                controller_load=defaultdict(int)
                deploy_flow_number=0
                chooses=[]
                mmm=len(source_random)*paths
                for i,v in enumerate(prob.variables()):#[begin:-1])

                    if i<mmm:
                       #print i
                       xp[i/3][i%3]=v.varValue
                for xpp in xp:
                    choose=4#4代表控制器
                    for j in range(0,3):
                        if xpp[j]==1.0:
                           choose=j
                           deploy_flow_number+=1
                    if choose==4:
                        uname=random.randint(0,unum-1)
                        if controller_load[uname]<=cu:
                            controller_load[uname]+=1
                        else:
                            path_random=random.randint(0,2)
                            choose=path_random
                            deploy_flow_number+=1
                    chooses.append(choose)
                alg2[random_time]=chooses
                flow_number[num_flow]=deploy_flow_number

    p2 = "./paper_result/choosepath_" + str(num_flow) + ".json"
    fd = open(p2, 'a')
    fd.write(json.dumps(alg2))
    fd.close()

    p0 = "./paper_result/edge_" + str(num_flow) + ".json"
    fd = open(p0, 'a')
    fd.write(json.dumps(alg0))
    fd.close()

    p3 = "./paper_result/switch_" + str(num_flow) + ".json"
    fd = open(p3, 'a')
    fd.write(json.dumps(alg1))
    fd.close()

    p1 = "./paper_result/objective_" + str(num_flow) + ".json"
    fd = open(p1, 'a')
    fd.write(json.dumps(objective))
    fd.close()



                # used_ce=defaultdict(int)
                # lambda1=0
                # for edge in all_edge:
                #     used_ce[edge]=0
                # for i in range(0,num_flow):
                #   for j in range(0,3):
                #     if x[i][j]==1.0:
                #         choose=j
                #   for edge in all_edge_alone[3*i+choose]:
                #       used_ce[edge]=used_ce[edge]+weight[i]
                #       if used_ce[edge]/float(ce)>lambda1:
                #             lambda1=used_ce[edge]/float(ce)
                # p1 = "./paper_result/alg0_" + str(num_flow) + ".json"  # rounding
                # fd = open(p1, 'a')
                # fd.write(json.dumps(lambda1))
                # fd.write(json.dumps("/"))
                # fd.close()
                # alg0 = alg0 + lambda1  # 应该是吞吐量

                



number_of_flow=[6000]
ce=100
cu=18000
unmu=5
big=0.5
small=0.03
entries=6500#交换机负载
paths=3#路径数
d=0.8
for num in number_of_flow:
    action(num,paths,flow_traffic=1,repeat_time=3,ce=ce,cu=cu,unum=unmu,big=big,small=small,entries=entries,d=d)
p4 = "./Data/deploy_flow_number.json"
save(p4,flow_number)
print "end"