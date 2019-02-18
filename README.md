# spanning-tree-using-Docker-and-AWS
root@ubuntu:~/mystp# docker build . -t my_spanning_tree_4 

Sending build context to Docker daemon  4.096kB 

Step 1/5 : FROM ubuntu 

---> 47b19964fb50 

Step 2/5 : RUN apt-get update 

---> Using cache 

---> 915aa5012883 

Step 3/5 : RUN apt-get install -y python 

---> Using cache 

---> 4505e951daa7 

Step 4/5 : COPY stp.py /opt/stp.py 

---> Using cache 

---> b3b4ee4b8668 

Step 5/5 : CMD ["python","/opt/stp.py"] 

---> Running in 58fa4ddbd58b 

Removing intermediate container 58fa4ddbd58b 

---> 86521bc3187f 

Successfully built 86521bc3187f 

Successfully tagged my_spanning_tree_4:latest 

root@ubuntu:~/mystp# docker run my_spanning_tree_4 

2 --- 3 

0 --- 3 

0 --- 1 

root@ubuntu:~/mystp#  

 
