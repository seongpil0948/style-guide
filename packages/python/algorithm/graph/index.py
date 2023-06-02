""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
https://www.geeksforgeeks.org/graph-and-its-representations/
"""

# A class to represent the adjacency list of the node 
class AdjNode: 
	def __init__(self, data): 
		self.vertex = data 
		self.next = None


# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
	def __init__(self, vertices): 
		self.V = vertices 
		self.graph = [None] * self.V 

	# Function to add an edge in an undirected graph 
	def add_edge(self, src, dest):  
		node = AdjNode(dest)

		node.next = self.graph[src] 
		self.graph[src] = node 

		# Adding the source node to the destination as 
		# it is the undirected graph 
		node = AdjNode(src) 
		node.next = self.graph[dest] 
		self.graph[dest] = node 

	# Function to print the graph 
	def print_graph(self): 
		for i in range(self.V): 
			print("Adjacency list of vertex {}\n head".format(i), end="") 
			temp = self.graph[i] 
			while temp: 
				print(" -> {}".format(temp.vertex), end="") 
				temp = temp.next
			print(" \n") 


# Driver program to the above graph class 
if __name__ == "__main__": 
    V = 5
    # five v
    graph = Graph(V) 
    #  Graph.graph[0] = Adj{ data: 1, next: Graph.graph[0] }
    #  Graph.graph[1] = Adj{ data: 0, next: Graph.graph[1] }
    graph.add_edge(src=0, dest=1) 
    graph.print_graph()
    # graph 0 index is added four's vertex 
    graph.add_edge(0, 4)
    graph.print_graph() 
    graph.add_edge(1, 2)
    graph.print_graph() 
    graph.add_edge(1, 3)
    graph.print_graph() 
    graph.add_edge(1, 4)
    graph.print_graph() 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 

    graph.print_graph() 

# This code is contributed by Kanav Malhotra 
