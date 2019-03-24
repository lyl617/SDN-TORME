import random
import matplotlib  
import numpy as np
import matplotlib.pyplot as pl

import pickle

import time


font = {'family' : 'serif',  
        'color'  : 'black',  
        'weight' : 'bold',  
        'size'   : 22,  
        }  


# t1 = time.time()
# # flow_entry_normal = pickle.load(open("flow_entry_normal.dat", "rb"))
# # flow_entry_hybrid = pickle.load(open("flow_entry_hybrid.dat", "rb"))
# # path_len = pickle.load(open("path_len.dat", "rb"))
# # print "dump1: %.3fs" % (time.time() - t1)

# t1 = time.time()
# x_normal = flow_entry_normal.keys()


# x_hybrid = flow_entry_hybrid.keys()

# y_normal = flow_entry_normal.values()

# y_hybrid = flow_entry_hybrid.values()


#----------------- normal data------------------
# number_of_flow = [10000,12000,14000,16000,18000]
# total_flowEntry_number_normal = [49804,59633,69584,79388,89493]
# total_flowEntry_number_hybrid = [23747,28443,33346,37887,42792]
# max_flow_normal = [2937,3542,4036,4718,5160]
# max_flow_hybrid = [916,1077,1257,1494,1591]


# number_of_flow_str = [10,12,14,16,18]

# average_switch_total_flowEntry_number_normal = [i / 100 for i in total_flowEntry_number_normal]
# average_switch_total_flowEntry_number_hybrid = [i / 100 for i in total_flowEntry_number_hybrid]

#---------------------fat tree data-------------------


# number_of_flow = [4000,6000,8000,10000,12000]
# total_flowEntry_number_normal = [24562,29422,39182,48914,58724]
# total_flowEntry_number_hybrid = [12800,15323,20428,25523,30602]



# number_of_flow_str = [4,6,8,10,12]

# average_switch_total_flowEntry_number_normal = [i / 80 for i in total_flowEntry_number_normal]
# average_switch_total_flowEntry_number_hybrid = [i / 80 for i in total_flowEntry_number_hybrid]


#-----------------------------------------------------------------------------
number_of_flow_origin = [10000,12000,14000,16000,18000]
number_of_flow_str_origin = [10,12,14,16,18]
max_flow_normal_origin = [2937,3542,4036,4718,5160]
max_flow_hybrid_origin = [916,1077,1257,1494,1591]


number_of_flow_fattree = [4000,6000,8000,10000,12000]
number_of_flow_str_fattree = [4,6,8,10,12]
max_flow_normal_fattree = [4842,5796,7710,9624,11556]
max_flow_hybrid_fattree = [974,1161,1550,1943,2312]


pl.figure(1)

pl.subplot(121)

normal = pl.plot(number_of_flow_str_origin,max_flow_normal_origin,'r*-',label="OSPF")
sr = pl.plot(number_of_flow_str_origin,max_flow_hybrid_origin,'gs-',label = "Hybrid Segment Routing")

pl.ylabel('Maximum Requied Flow Entries',fontdict = font)
pl.xlabel('Number of Flows(*10^3)',fontdict = font)

pl.legend(loc="best")



pl.subplot(122)

normal = pl.plot(number_of_flow_str_fattree,max_flow_normal_fattree,'r*-',label="OSPF")
sr = pl.plot(number_of_flow_str_fattree,max_flow_hybrid_fattree,'gs-',label = "Hybrid Segment Routing")

pl.ylabel('Maximum Requied Flow Entries',fontdict = font)
pl.xlabel('Number of Flows(*10^3)',fontdict = font)

pl.legend(loc="best")




pl.figure(2)



number_of_flow_str_origin = [10,12,14,16,18]
total_flowEntry_number_normal_origin = [49804,59633,69584,79388,89493]
total_flowEntry_number_hybrid_origin = [23747,28443,33346,37887,42792]
average_switch_total_flowEntry_number_normal_origin = [i / 100 for i in total_flowEntry_number_normal_origin]
average_switch_total_flowEntry_number_hybrid_origin = [i / 100 for i in total_flowEntry_number_hybrid_origin]


number_of_flow_str_fattree = [4,6,8,10,12]
total_flowEntry_number_normal_fattree = [24562,29422,39182,48914,58724]
total_flowEntry_number_hybrid_fattree = [12800,15323,20428,25523,30602]

average_switch_total_flowEntry_number_normal_fattree = [i / 80.0 for i in total_flowEntry_number_normal_fattree]
average_switch_total_flowEntry_number_hybrid_fattree = [i / 80.0 for i in total_flowEntry_number_hybrid_fattree]

print average_switch_total_flowEntry_number_normal_fattree
print average_switch_total_flowEntry_number_hybrid_fattree
#exit()

pl.subplot(121)
pl.plot(number_of_flow_str_origin,average_switch_total_flowEntry_number_normal_origin,\
		'r*-',label="OSPF")

pl.plot(number_of_flow_str_origin,average_switch_total_flowEntry_number_hybrid_origin,\
		'gs-',label = "Hybrid Segment Routing")

pl.xlabel('Number of Flows(*10^3)',fontdict = font)
pl.ylabel('Average Switch Flow Entry Required',fontdict = font)



pl.legend(loc="upper left")


pl.subplot(122)

pl.plot(number_of_flow_str_fattree,average_switch_total_flowEntry_number_normal_fattree,\
		'r*-',label="OSPF")

pl.plot(number_of_flow_str_fattree,average_switch_total_flowEntry_number_hybrid_fattree,\
		'gs-',label = "Hybrid Segment Routing")

pl.xlabel('Number of Flows(*10^3)',fontdict = font)
pl.ylabel('Average Switch Flow Entry Required',fontdict = font)



pl.legend(loc="upper left")




pl.show()


#-------------------------------

# pl.plot(number_of_flow_str,average_switch_total_flowEntry_number_normal,\
# 		'r*-',label="OSPF")

# pl.plot(number_of_flow_str,average_switch_total_flowEntry_number_hybrid,\
# 		'gs-',label = "Hybrid Segment Routing")

# pl.xlabel('Number of Flow',fontdict = font)
# pl.ylabel('Average Switch Flow Entry Requied',fontdict = font)



# pl.legend(loc="upper left")

# print "dump2: %.3fs" % (time.time() - t1)


