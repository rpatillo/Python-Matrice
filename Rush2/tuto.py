from pyglet.gl import *

class Triangle:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3, [-0.5, -0.5])

class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(400, 300)

if __name__ == "__main__":
    window = MyWindow(1280, 720, "My Pyglet Window", resizable=True)
    pyglet.app.run()