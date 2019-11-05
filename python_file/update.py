#!/usr/bin/python
#-*- coding:utf-8 -*-
import socket #socket.gethostname获取主机名，适用于Nwindows佒~Llinux           
import sys #sys.path获取系统路径          
import subprocess
import os
import json
import getpass


if not os.path.exists('/u01/HHT30/bak/20190925-v12.7'):
     os.mkdir('/u01/HHT30/bak/20190925-v12.7')
subprocess.call('sh /u01/HHT30/stop.sh',shell=True)
subprocess.call('cd /u01/HHT30',shell=True)
subprocess.call('pwd',shell=True)
res=subprocess.call('wget http://10.108.15.200/sss_new_dtx5-12.8.jar',shell=True)
subprocess.call('mv  sss_new_dtx5-12.0.jar /u01/HHT30/bak/20190925-v12.7',shell=True)
res2 = subprocess.call('sh /u01/HHT30/start.sh',shell=True)
#print(res2)
if res2:
        print('start fail')
        sys.exit(0)