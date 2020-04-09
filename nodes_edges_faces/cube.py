from wireframe import *

if __name__ == "__main__":
    CUBE_NODES = [(x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)]
    cube = Wireframe()
    cube.add_nodes(CUBE_NODES)
    cube.add_edges([(n, n+4) for n in range(0, 4)])
    cube.add_edges([(n, n+1) for n in range(0, 8, 2)])
    cube.add_edges([(n, n+2) for n in (0, 1, 4, 5)])

    cube.output_nodes()
    cube.output_edges()
