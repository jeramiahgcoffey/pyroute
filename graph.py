class Vertex:
    def __init__(self, label):
        self.label = label


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.distances = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, vertex_a, vertex_b, distance):
        self.distances[(vertex_a, vertex_b)] = distance
        self.distances[(vertex_b, vertex_a)] = distance
        self.adjacency_list[vertex_a].append(vertex_b)
        self.adjacency_list[vertex_b].append(vertex_a)
