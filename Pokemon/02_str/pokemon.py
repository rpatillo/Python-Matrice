class Pokemon:

    xp = 0

    def __init__(self, name, vocabulary=None):
        self.name = name
        if vocabulary != None:
            self.vocabulary = vocabulary
        else:
            self.vocabulary = name + ' ' + name

    def __str__(self):
        return(f'Pokemon {self.name} at lvl {self.xp // 100}')

    def talk(self):
        print(self.vocabulary)

    def shout(self):
        print(self.vocabulary.upper() + '!!!')
    
    def add_xp(self, xp):
        self.xp += xp
    
    def lvl(self):
        print(self.xp // 100)