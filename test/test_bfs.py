# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph("data/tiny_network.adjlist")
    out = g.bfs("Martin Kampmann")
    assert len(out) == 30 # assert all nodes were traversed
    kampmann_children = ['33483487', '32790644', '31806696', '31626775', '31540829']
    for kampmann_child in kampmann_children:
        assert kampmann_child in out[1:6] # assert search was breadth-first

def test_bfs():
    """
    Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    g = graph.Graph("data/tiny_network.adjlist")
    out = g.bfs("Martin Kampmann", "Luke Gilbert")
    # check that the shortest path was found
    assert len(out) == 3 
    assert out[0] == "Martin Kampmann"
    assert out[1] == "33483487"
    assert out[2] == "Luke Gilbert"

    # check that None is returned when no path is found
    out = g.bfs("Martin Kampmann", "Thomas Mazumder")
    assert out == None
