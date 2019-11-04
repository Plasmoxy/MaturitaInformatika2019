from math import pi, sin, cos

import pyglet
from pyglet.gl import *

try:
    # Try and create a window with multisampling (antialiasing)
    config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True)
    window = pyglet.window.Window(resizable=True, config=config)
except pyglet.window.NoSuchConfigException:
    # Fall back to no multisampling for old hardware
    window = pyglet.window.Window(resizable=True)

# Change the window projection to 3D:
window.projection = pyglet.window.Projection3D()



@window.event
def on_draw():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -4)
    glRotatef(rz, 0, 0, 1)
    glRotatef(ry, 0, 1, 0)
    glRotatef(rx, 1, 0, 0)
    batch.draw()


def update(dt):
    global rx, ry, rz
    rx += dt * 1
    ry += dt * 80
    rz += dt * 30
    rx %= 360
    ry %= 360
    rz %= 360


def setup():
    # One-time GL setup
    glClearColor(1, 1, 1, 1)
    glColor3f(1, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)

    # Uncomment this line for a wireframe view
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    # Simple light setup.  On Windows GL_LIGHT0 is enabled by default,
    # but this is not the case on Linux or Mac, so remember to always 
    # include it.
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)


def create_torus(radius, inner_radius, slices, inner_slices, batch):

    # Create the vertex and normal arrays.
    vertices = []
    normals = []

    u_step = 2 * pi / (slices - 1)
    v_step = 2 * pi / (inner_slices - 1)
    u = 0.
    for i in range(slices):
        cos_u = cos(u)
        sin_u = sin(u)
        v = 0.
        for j in range(inner_slices):
            cos_v = cos(v)
            sin_v = sin(v)

            d = (radius + inner_radius * cos_v)
            x = d * cos_u
            y = d * sin_u
            z = inner_radius * sin_v

            nx = cos_u * cos_v
            ny = sin_u * cos_v
            nz = sin_v

            vertices.extend([x, y, z])
            normals.extend([nx, ny, nz])
            v += v_step
        u += u_step

    # Create a list of triangle indices.
    indices = []
    for i in range(slices - 1):
        for j in range(inner_slices - 1):
            p = i * inner_slices + j
            indices.extend([p, p + inner_slices, p + inner_slices + 1])
            indices.extend([p, p + inner_slices + 1, p + 1])

    # Create a Material and Group for the Model
    diffuse = [0.0, 1.0, 0.0, 0.5]
    ambient = [0.5, 0.0, 0.3, 1.0]
    specular = [1.0, 1.0, 1.0, 1.0]
    emission = [0.0, 0.0, 0.0, 1.0]
    shininess = 50
    material = pyglet.model.Material("", diffuse, ambient, specular, emission, shininess)
    group = pyglet.model.MaterialGroup(material=material)

    vertex_list = batch.add_indexed(len(vertices)//3,
                                    GL_TRIANGLES,
                                    group,
                                    indices,
                                    ('v3f/static', vertices),
                                    ('n3f/static', normals))

    return pyglet.model.Model([vertex_list], [group], batch)


setup()
batch = pyglet.graphics.Batch()
torus_model = create_torus(1, 0.3, 50, 30, batch=batch)
torus_model2 = create_torus(3, 0.1, 20, 40, batch=batch)
torus_model3 = create_torus(0.1, 0.4, 50, 30, batch=batch)
rx = ry = rz = 0

pyglet.clock.schedule(update)

pyglet.app.run()