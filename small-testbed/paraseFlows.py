#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 4:01 PM
# @Author  : Jsen617
# @Site    : 
# @File    : paraseFlows.py.py
# @Software: PyCharm
from collections import defaultdict
class paraseFlows(object):
    def readFile(self,pathname):
        flows_fct = defaultdict(lambda : 0)
        f = open(pathname,'r')
        flows = f.readlines()
        for flow in flows:
            flow_info = flow.split(" ")
            fct = int(flow_info[1])
            if fct < 1000:
                flows_fct[1] += 1
            elif fct >= 1000 and fct <= 10000:
                flows_fct[2] += 1
            elif fct >= 10000 and fct <= 100000:
                flows_fct[3] += 1
            elif fct >= 100000 and fct <= 1000000:
                flows_fct[4] += 1
            else:
                flows_fct[5] += 1
        f.close()
        print(flows_fct)
if __name__ == "__main__":
    pf = paraseFlows()
    pf.readFile("data/jvrp_flows30s.txt")
    pf.readFile("data/match_flows30s.txt")
    pf.readFile("data/simple_flows30s.txt")