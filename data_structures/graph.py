class Vertex:
    """Models Vertex objects to be used with a Graph."""

    def __init__(self, label):
        """
        Initialize Vertex objects.

        :param label: String. The name of the vertex.
        """
        self.label = label


class Graph:
    """Models an undirected graph of Vertices(addresses) and edges(distances)"""

    def __init__(self):
        """
        Initialize Graph objects.

        Set adjacency list and distances to empty dictionaries.
        """

        self.adjacency_list = {}
        self.distances = {}

    def add_vertex(self, vertex):
        """
        Add a Vertex to the adjacency list, set its value as an empty array.

        :param vertex: Vertex object to add to the adjacency list.
        """

        self.adjacency_list[vertex.label] = []

    def add_edge(self, vertex_a, vertex_b, distance):
        """
        Add an edge to the 'distances' dictionary, representing the distance between two Vertices.

        :param vertex_a: A Vertex object.
        :param vertex_b: A Vertex object.
        :param distance: String. The distance between the two Vertices.
        """

        self.distances[(vertex_a.label, vertex_b.label)] = distance
        self.distances[(vertex_b.label, vertex_a.label)] = distance
        self.adjacency_list[vertex_a.label].append(vertex_b.label)
        self.adjacency_list[vertex_b.label].append(vertex_a.label)

