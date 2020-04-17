import numpy as np
import math

class Wireframe:
    """
    A wireframe is a 3d object only composed of nodes and edges.
    Wireframes do not possess any faces.
    """
    def __init__(self):
        self.nodes = np.zeros((0, 4))
        self.edges = []

    """
    Adds a list of nodes to the existing set of nodes.
    """
    def add_nodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))

    """
    Adds a list of edges to the existing set of edges.
    """
    def add_edges(self, edge_list):
        self.edges += edge_list

    """Outputs all of the values for every existing node."""
    def output_nodes(self):
        print("\n --- Nodes --- ")
        for i, (x, y, z, _) in enumerate(self.nodes):
            print(f"{i}: ({x}, {y}, {z})")

    """Outputs all of the edges for every existing edge set."""
    def output_edges(self):
        print("\n --- Edges --- ")
        for i, (node1, node2) in enumerate(self.edges):
            print(f"   {i}: {node1} -> {node2}")
    
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
            node.x = cx + d * np.cos(theta)
            node.y = cy + d * np.sin(theta)

    def rotate_x(self, centers, radians):
        for node in self.nodes:
            cx, cy, cz = centers
            y = node.y - cy
            z = node.z - cz
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            node.z = cz + d * np.cos(theta)
            node.y = cy + d * np.sin(theta)

    def rotate_y(self, centers, radians):
        for node in self.nodes:
            cx, cy, cz = centers
            x = node.x - cx
            z = node.z - cz
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            node.z = cz + d * np.cos(theta)
            node.x = cx + d * np.sin(theta)


if __name__ == "__main__":
    """With the current setup, we can add three nodes and
    create an edge between the second two like so:"""
    cube = Wireframe()
    cube_nodes = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    cube.add_nodes(np.array(cube_nodes))
    cube.add_edges([(n, n+4) for n in range(0, 4)])
    cube.add_edges([(n, n+1) for n in range(0, 8, 2)])
    cube.add_edges([(n, n+2) for n in (0, 1, 4, 5)])
    cube.output_nodes()
    cube.output_edges()
