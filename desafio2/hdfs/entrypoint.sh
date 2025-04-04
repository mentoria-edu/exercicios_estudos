#!/bin/bash

set -e 

service ssh start && start-dfs.sh

sleep 10

sudo -u hdfs opt/hadoop/bin/hadoop fs -mkdir /warehouse
sudo -u hdfs /opt/hadoop/bin/hadoop fs -setfacl -m user:hive:rwx /warehouse

tail -f /dev/null
