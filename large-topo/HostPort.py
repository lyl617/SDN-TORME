import cPickle as pickle
import random
import json
from collections import defaultdict
Hosts=defaultdict(lambda :defaultdict(int))
def save(path,con):
    fd = open(path, 'a')
    fd.write(json.dumps(con))
    fd.close()
def genport(num_flow):
   prefix="./paper_data2/"
   source_random_file = prefix + "source_random_" + str(num_flow) + ".dat"
   terminal_random_file = prefix + "terminal_random_" + str(num_flow) + ".dat"
   source_random = pickle.load(open(source_random_file, "rb"))
   terminal_random=pickle.load(open(terminal_random_file,"rb"))

   for i in range(num_flow):
       hsport = []#srchost,deshost,srcport,desport
       srcport=random.randint(1024,65535)
       desport=random.randint(1024,65535)
       hsport.append(source_random[i])
       hsport.append(terminal_random[i])
       hsport.append(srcport)
       hsport.append(desport)
       Hosts[num_flow][i]=hsport
num_flows=[4000,6000,8000,10000,12000]
for num in num_flows:
    genport(num)
save('./Data/hsport.json',Hosts)
