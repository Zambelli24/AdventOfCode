import networkx as nx
from aocd import get_data

def get_all_connections():
  raw_data = get_data(year=2023, day=25).splitlines()

  all_connections = []

  for row in raw_data:
    component, connections = row.split(': ')
    connections = connections.split(' ')

    for connection in connections:
      all_connections.append((component, connection))

  print('---------- ALL CONNECTIONS ----------')
  print(all_connections)
  return all_connections

def build_graph():
  connections = get_all_connections()
  graph = nx.Graph()
  for connection in connections:
    graph.add_edge(connection[0], connection[1])
  
  print('---------- GRAPH ----------')
  print(graph)
  return graph

def find_and_cut_edges():
  graph = build_graph()
  graph.remove_edges_from(nx.minimum_edge_cut(graph))

  size_product = 1
  for group in nx.connected_components(graph):
    print('---------- GROUP ----------')
    print(len(group))
    size_product *= len(group)

  print('---------- GROUP SIZE PRODUCT ----------')
  print(size_product)
  return size_product

find_and_cut_edges()