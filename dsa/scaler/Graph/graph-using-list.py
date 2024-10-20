class Graph:

    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_lis = {}

        for node in self.nodes:
            self.adj_lis[node] = []

    def print_adj_list(self):
        for node in self.nodes:
            print(node, '-->', self.adj_lis[node])

    def add_edges(self, u, v):
        self.adj_lis[u].append(v)
        self.adj_lis[v].append(u)

nodes = ['A', 'B', 'C', 'D', 'E', 'F']
graph = Graph(nodes)

all_edges = [['A','B'], ['A','C'],['B','D'],['C','D'],['C','E'],['D','E']]

for u,v in all_edges:
    graph.add_edges(u, v)

graph.print_adj_list()
