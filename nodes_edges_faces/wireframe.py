import math

class Node:
    """
    Nodes refer to single points in 3d space with three coordinates.
    These coordinates are x, y, and z.
    """
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]

class Edge:
    """
    Edges, also called vertices, are lines that connect two nodes.
    """
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

class Wireframe:
    """
    A wireframe is a 3d object only composed of nodes and edges.
    Wireframes do not possess any faces.
    """
    def __init__(self):
        self.nodes = []
        self.edges = []

    """
    Adds a list of nodes to the existing set of nodes.
    """
    def add_nodes(self, node_list):
        for node in node_list:
            self.nodes.append(Node(node))

    """
    Adds a list of edges to the existing set of edges.
    """
    def add_edges(self, edge_list):
        for (start, stop) in edge_list:
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))

    """Outputs all of the values for every existing node."""
    def output_nodes(self):
        print("\n --- Nodes --- ")
        for i, node in enumerate(self.nodes):
            print(f"{i}: ({node.x:.2f}, {node.y:.2f}, {node.z:.2f})")

    """Outputs all of the edges for every existing edge set."""
    def output_edges(self):
        print("\n --- Edges --- ")
        for i, edge in enumerate(self.edges):
            print(f" {i}: ({edge.start.x}, {edge.start.y}, {edge.start.z})")
            print(f"to ({edge.stop.x}, {edge.stop.y}, {edge.stop.z})")
    
    def translate(self, axis, d):
        """ Translate each node of a wireframee by d along a given axis. """

        if axis in ['x', 'y', 'z']:
            for node in self.nodes:
                setattr(node, axis, getattr(node, axis) + d)
    
    def scale(self,  centers, scale):
        """ Scale the wireframe from the center of the screen. """

        for node in self.nodes:
            node.x = centers[0] + scale * (node.x - centers[0])
            node.y = centers[1] + scale * (node.y - centers[1])
            node.z *= scale

    def find_center(self):
        """
        Find the center of the wireframe.
        """
        
        num_nodes = len(self.nodes)
        mean_x = sum([node.x for node in self.nodes]) / num_nodes
        mean_y = sum([node.y for node in self.nodes]) / num_nodes
        mean_z = sum([node.z for node in self.nodes]) / num_nodes

        return (mean_x, mean_y, mean_z)

    def rotate_z(self, centers, radians):
        for node in self.nodes:
            cx, cy, cz = centers
            x = node.x - cx
            y = node.y - cy
            d = math.hypot(y, x)
            theta = math.atan2(y, x) + radians
            node.x = cx + d * math.cos(theta)
            node.y = cy + d * math.sin(theta)

    def rotate_x(self, centers, radians):
        for node in self.nodes:
            cx, cy, cz = centers
            y = node.y - cy
            z = node.z - cz
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            node.z = cz + d * math.cos(theta)
            node.y = cy + d * math.sin(theta)

    def rotate_y(self, centers, radians):
        for node in self.nodes:
            cx, cy, cz = centers
            x = node.x - cx
            z = node.z - cz
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            node.z = cz + d * math.cos(theta)
            node.x = cx + d * math.sin(theta)


if __name__ == "__main__":
    """With the current setup, we can add three nodes and
    create an edge between the second two like so:"""
    my_wireframe = Wireframe()
    my_wireframe.add_nodes([(0, 0, 0), (1, 2, 3), (3, 2, 1)])
    my_wireframe.add_edges([(1, 2)])

    my_wireframe.output_nodes()
    my_wireframe.output_edges()
