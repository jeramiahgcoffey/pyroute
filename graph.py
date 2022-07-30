class Vertex:
    """This class represents Vertices"""

    def __init__(self, label):
        """
        The constructor for the Vertex class

        :param label: The name of the vertex
        """
        self.label = label


class Graph:
    """This class represents an undirected graph of Vertices(addresses) and edges(distances)"""

    def __init__(self):
        """
        The constructor for the Graph class

        Sets adjacency list and distances to empty dictionaries
        """

        self.adjacency_list = {}
        self.distances = {}

    def add_vertex(self, vertex):
        """
        This method adds a Vertex to the adjacency list, setting its value as an empty array

        :param vertex: A Vertex object to add to the adjacency list
        :return: Boolean representing a successful addition (always True)
        """

        self.adjacency_list[vertex.label] = []
        return True

    def add_edge(self, vertex_a, vertex_b, distance):
        """
        This method adds an edge to the 'distances' dictionary, representing the distance between two Vertices

        :param vertex_a: A Vertex object
        :param vertex_b: A Vertex object
        :param distance: The distance between the two Vertices
        :return: Boolean representing a successful addition (always True)
        """

        self.distances[(vertex_a.label, vertex_b.label)] = distance
        self.distances[(vertex_b.label, vertex_a.label)] = distance
        self.adjacency_list[vertex_a.label].append(vertex_b.label)
        self.adjacency_list[vertex_b.label].append(vertex_a.label)
        return True

