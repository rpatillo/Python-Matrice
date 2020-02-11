class Pokemon:

    def __init__(self, name, vocabulary=None):
        self.name = name
        if vocabulary != None:
            self.vocabulary = vocabulary
        else:
            self.vocabulary = name + ' ' + name

    def talk(self):
        print(self.vocabulary)

    def shout(self):
        print(self.vocabulary.upper() + '!!!')