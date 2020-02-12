import pyglet
# from pyglet.gl import *
from pyglet.window import key

class Main():

    SWIDTH = 50
    SHEIGHT = 50
    START_X = 0
    START_Y = 0    

    decal_x = 0
    decal_y = 0

    def __init__(self):
        self.window = pyglet.window.Window()
        self.label = pyglet.text.Label("0", font_size=36, x=self.window.width // 2, y=self.window.height // 2)
        self.window.event(self.on_text_motion)
        self.window.event(self.on_draw)
        self.fps_display = pyglet.window.FPSDisplay(self.window)
        pyglet.clock.schedule(self.game_loop)
        pyglet.app.run()

    def on_text_motion(self, motion):
        if motion == key.UP:
            self.decal_y += 10
        if motion == key.DOWN:
            self.decal_y -= 10
        if motion == key.LEFT:
            self.decal_x -= 10
        if motion == key.RIGHT:
            self.decal_x += 10

    def on_draw(self):
        self.window.clear()
        self.quad.draw(pyglet.gl.GL_QUADS)
        self.label.draw()
        self.fps_display.draw()

    def game_loop(self, _):
        self.label.text = str(int(self.label.text) + 1)
        self.quad = pyglet.graphics.vertex_list(4,
        ('v2i', (self.START_X + self.decal_x, self.START_Y + self.decal_y,  
                self.START_X + self.SWIDTH + self.decal_x, self.START_Y + self.decal_y, 
                self.START_X + self.SWIDTH + self.decal_x, self.START_Y + self.SHEIGHT + self.decal_y, 
                self.START_X + self.decal_x, self.START_Y + self.SHEIGHT + self.decal_y)),
        # ('v2i', (10, 10,  100, 10, 100, 100, 10, 100)),
        ('c3B', (0, 0, 255)*4)
        )


Main()


    # def on_key_press(self, symbol, modifiers):
    #     if symbol == key.UP:
    #         self.decal_x += 5
    #     if symbol == key.DOWN:
    #         self.decal_x -= 5
    #     if symbol == key.LEFT:
    #         self.decal_y -= 5
    #     if symbol ==key.RIGHT:
    #         self.decal_y += 5

    
    # quad = pyglet.graphics.vertex_list(4,
    # ('v2i', (self.START_X + self.decal_x, self.START_Y + self.decal_y,  
    #         self.START_X + self.SWIDTH + self.decal_x, self.START_Y + self.decal_y, 
    #         self.START_X + self.SWIDTH + self.decal_x, self.START_Y + self.SHEIGHT + self.decal_y, 
    #         self.START_X + self.decal_x, self.START_Y + self.SHEIGHT + self.decal_y)),
    # # ('v2i', (10, 10,  100, 10, 100, 100, 10, 100)),
    # ('c3B', (0, 0, 255)*4)
    # )