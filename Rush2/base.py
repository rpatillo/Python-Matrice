import pyglet

class Base:
    HEIGHT = 600
    WIDTH = 800

    def __init__(self):
        self.window = pyglet.window.Window(Base.WIDTH, Base.HEIGHT)
        self.label = pyglet.text.Label("0", font_size=36, x=Base.WIDTH / 2, y=Base.HEIGHT / 2)
        self.sprite = pyglet.sprite.Sprite(img=pyglet.resource.image('images/image.png'))
        self.texte = pyglet.text.Label('Hello, word!',
                                        font_name='Times New Roman',
                                        font_size=36,
                                        x = 10, y=10)
        self.window.event(self.on_draw)
        pyglet.clock.schedule(self.game_loop)

        pyglet.app.run()



    def on_draw(self):
        self.window.clear()
        self.sprite.draw()
        self.label.draw()
        self.texte.draw()



    def game_loop(self, _):
        self.label.text = str(int(self.label.text) + 1)

Base()