import pygame
from nodes_edges_faces import wireframe

class ProjectionViewer:
    """ Displays 3D objects on a Pygame screen """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Wireframe Display')
        self.background = (10, 10, 50)

        self.wireframes = {}
        self.display_nodes = True
        self.display_edges = True
        self.node_color = (255, 255, 255)
        self.edge_color = (200, 200, 200)
        self.node_radius = 4
    
    def run(self):
        """ Create a pygame screen until it is closed."""

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display()
            pygame.display.flip()
    
    def addWireFrame(self, name, wireframe):
        """Add a named wireframe object."""
        self.wireframes[name] = wireframe

    def display(self):
        """ Draw the wireframes on the screen. """

        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            if self.display_edges:
                for edge in wireframe.edges:
                    pygame.draw.aaline(self.screen, self.edge_color, (edge.start.x, edge.start.y), (edge.stop.x, edge.stop.y), 1)

            if self.display_nodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.node_color, (int(node.x), int(node.y)), self.node_radius, 0)

if __name__ == '__main__':
    cube = wireframe.Wireframe()
    cube.add_nodes([(x,y,z) for x in (50, 250) for y in (50, 250) for z in (50, 250)])
    cube.add_edges([(n, n+4) for n in range(0, 4)] + [(n, n+1) for n in range(0, 8, 2)] + [(n, n+2) for n in (0, 1, 4, 5)])

    pv = ProjectionViewer(400, 300)
    pv.addWireFrame('cube', cube)
    pv.run()
