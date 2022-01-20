import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object which serves as a container for 
        methods to load data and 
        
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
    
    def shortest_path(self, start, end, pred):
        path = []
        path.append(end)
        while path[-1] != start:
            path.append(pred[path[-1]])
        return path[::-1]

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None
        """
        visited = dict(zip(list(self.graph.nodes),[False]*len(self.graph.nodes)))
        queue = list()
        pred = dict()
        traversal = []
        
        queue.append(start)
        visited[start] = True
        
        while len(queue) != 0:
            v = queue.pop(0)
            traversal.append(v)
            for successor in self.graph.successors(v):
                if not visited[successor]:
                    visited[successor] = True
                    pred[successor] = v
                    queue.append(successor)
                    
                    if successor == end:
                        return self.shortest_path(start, end, pred)
                    
        if end == None:
            return traversal
        else:
            return None
        return




