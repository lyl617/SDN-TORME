from graph_for_l2 import DiGraph
from collections import defaultdict
import json
import random
import  cPickle as pickle

'''
this code is generating a fat tree topology, stores in json format.
example:
                  switch                 switch               switch               switch
                  .    .                 .    .               .    .               .    .
                .        .             .        .           .        .           .        .
            switch      switch    switch      switch    switch      switch    switch      switch
              .           .         .           .         .           .         .           .
              .  .     .  .         .  .     .  .         .  .     .  .         .  .     .  .
              .    ..     .         .    ..     .         .    ..     .         .    ..     .
              .   .  .    .         .   .  .    .         .   .  .    .         .   .  .    .
              . .      .  .         . .      .  .         . .      .  .         . .      .  .
            switch      switch    switch     switch      switch    switch     switch       switch
            .    .      .    .    .    .     .    .      .    .    .    .     .    .       .    .
            .    .      .    .    .    .     .    .      .    .    .    .     .    .       .    .
          host host   host host  host host  host host   host host host host  host host    host host
'''
CODEC='utf-8'
hosts=[]
switchs=[]
topology_name='fat_tree'
switch_net=defaultdict(lambda :defaultdict(lambda :1))

def addEdge(net,src,des):
    net[src][des]=1
    net[des][src]=1

def nameOfSwitch(node):
    return 'v'+str(node)

def nameOfHost(node):
    return 'h'+str(node)

core_number=16
secondLevel_number=core_number*2
cell_number=4
#add switch
for i in range(0,core_number+secondLevel_number*2):
    switchs.append(i)

for i,core in enumerate(switchs[0:core_number]):
    for des in switchs[core_number:core_number+secondLevel_number]:
        addEdge(switch_net,nameOfSwitch(core),nameOfSwitch(des))
#print switch_net['v48']
for node in switchs[core_number:core_number+secondLevel_number]:
    addEdge(switch_net,nameOfSwitch(node),nameOfSwitch(node+secondLevel_number))
    if node%2==0:
        addEdge(switch_net,nameOfSwitch(node),nameOfSwitch(node+secondLevel_number+1))
    else:
        addEdge(switch_net,nameOfSwitch(node),nameOfSwitch(node+secondLevel_number-1))

#add host
for i in range(0,core_number*2*cell_number):
    hosts.append(i)

temp=[]
for h in hosts:
    temp.append(nameOfHost(h))
json.dump(temp,open(topology_name+'_host'+'.json','w'))

i=0
for node in switchs[core_number+secondLevel_number:]:
    for t in range(0,4):
        addEdge(switch_net,nameOfSwitch(node),nameOfHost(hosts[i]))
        i+=1
print switch_net['h10']
json.dump(switch_net,open(topology_name+'.json','w'))

