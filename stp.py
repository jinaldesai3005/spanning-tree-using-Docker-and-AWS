
class Graph: 
  
  def __init__(self,vertices): 
    self.V= vertices #No. of vertices 
    self.graph = [] # default dictionary  
                                # to store graph 
          
   
    # function to add an edge to graph 
  def addEdge(self,u,v,w): 
    self.graph.append([u,v,w]) 
  def KruskalMST(self): 
  
    result =[] #This will store the resultant MST 
    self.graph = (sorted(self.graph,key=lambda item: item[2]))
   
    edges=[]
    for i in self.graph:
      i=i[0:2]#ignore the last element in each list which is cost metric
      edges.append(i)
    
    a=[]
    l=[]
    for i in ((edges)):#pick each element and check if its forming a closed loop
      if ( i[0] in a) and ( i[1] in a):
        continue
      else:

        a.append(i[0])
        a.append(i[1])
        l.append(i)
    for i in l:
      print(("%s --- %s")%(i[0],i[1]))
    
      

    
      
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
g.KruskalMST()
