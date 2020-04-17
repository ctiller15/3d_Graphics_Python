import numpy as np
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

                elif event.type == pygame.KEYDOWN:
                    if event.key in key_to_function:
                        key_to_function[event.key](self)

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
                for n1, n2 in wireframe.edges:
                    pygame.draw.aaline(self.screen, self.edge_color, wireframe.nodes[n1][:2], wireframe.nodes[n2][:2], 1)

            if self.display_nodes:
                for node in wireframe.nodes:
                    pygame.draw.circle(self.screen, self.node_color, (int(node[0]), int(node[1])), self.node_radius, 0)

    def translateAll(self, axis, d):
        """ Translate all wireframes along a given axis by d units. """

        for wireframe in self.wireframes.values():
            wireframe.translate(axis, d)

    def scaleAll(self, scale):
        """ Scale all wireframes by a given scale, centered on the center of the screen. """

        center_x = self.width/2
        center_y = self.height / 2

        for wireframe in self.wireframes.values():
            wireframe.scale((center_x, center_y), scale)

    def rotate_all(self, axis, theta):
        """
        Rotate all wireframe about their center, along a given axis by a given angle.
        """

        rotate_function = 'rotate_' + axis

        for wireframe in self.wireframes.values():
            center = wireframe.find_center()
            getattr(wireframe, rotate_function)(center, theta)

key_to_function = {
        pygame.K_LEFT: (lambda x: x.translateAll('x', -10)),
        pygame.K_RIGHT: (lambda x: x.translateAll('x', 10)),
        pygame.K_DOWN: (lambda x: x.translateAll('y', 10)),
        pygame.K_UP: (lambda x: x.translateAll('y', -10)),
        pygame.K_EQUALS: (lambda x: x.scaleAll(1.25)),
        pygame.K_MINUS: (lambda x: x.scaleAll(0.8)),

        pygame.K_q: (lambda x: x.rotate_all('x', 0.1)),
        pygame.K_w: (lambda x: x.rotate_all('x', -0.1)),
        pygame.K_a: (lambda x: x.rotate_all('y', 0.1)),
        pygame.K_s: (lambda x: x.rotate_all('y', -0.1)),
        pygame.K_z: (lambda x: x.rotate_all('z', 0.1)),
        pygame.K_x: (lambda x: x.rotate_all('z', -0.1)),
        }
if __name__ == '__main__':
    cube = wireframe.Wireframe()
    
    cube.add_nodes(np.array([(x,y,z) for x in (50, 250) for y in (50, 250) for z in (50, 250)]))
    cube.add_edges([(n, n+4) for n in range(0, 4)] + [(n, n+1) for n in range(0, 8, 2)] + [(n, n+2) for n in (0, 1, 4, 5)])

    # cube.translate('x', 100)
    # cube.translate('y', -40)

    # cube.scale((200, 150), .75)

    # cube.rotateZ(cube.find_center(), 0.1)

    pv = ProjectionViewer(400, 300)
    pv.addWireFrame('cube', cube)
    pv.run()
