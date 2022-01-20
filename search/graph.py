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
        """
        Auxiliary method used in bfs(). Given dictionary of predecessors, start,
        and end, trace the shortest path
        """
        path = []
        path.append(end)
        while path[-1] != start:
            path.append(pred[path[-1]])
        return path[::-1]

    def bfs(self, start, end=None):
        """
        write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node, just return a list with the order of traversal
        * If there is an end node and a path exists, return a list of the shortest path
        * If there is an end node and a path does not exist, return None
        """
        # set up the data structures
        visited = dict(zip(list(self.graph.nodes),[False]*len(self.graph.nodes)))
        queue = list()
        pred = dict()
        traversal = []
        
        # initialize the queue with the start node
        queue.append(start)
        visited[start] = True
        
        # conduct the breadth-first search
        while len(queue) != 0:
            v = queue.pop(0)
            traversal.append(v)
            # loop through all the children of the node, adding them to queue
            for successor in self.graph.successors(v):
                if not visited[successor]:
                    visited[successor] = True
                    pred[successor] = v
                    queue.append(successor)
                    # if the end node is found, the search is done
                    if successor == end:
                        return self.shortest_path(start, end, pred)
        
        # if no end node is given, return the list of nodes in the order traversed             
        if end == None:
            return traversal
        # if an end node was given but not found, return None
        else:
            return None
        return




