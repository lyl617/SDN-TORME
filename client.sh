#!/bin/bash
for((i=1;i<300;i++));
do
    iperf -c $1 -p 1000 -t 0.01
done
