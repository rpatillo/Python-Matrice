import sys
from pokemon import Pokemon

class Pokeball:

    pokemon = None

    def __init__(self, pokemon=None):
        if pokemon != None:
            self.store(pokemon)
        
    def __str__(self):
        if self.pokemon == None:
            return("An empty pokeball")
        else:
            return(str(self.pokemon))

    def store(self, pokemon):
        if self.pokemon != None:
            print("Two pokemons in the same pokeball is barbary!")
        else:
            self.pokemon = pokemon

    def release(self):
        if self.pokemon != None:
            temp = self.pokemon
            self.pokemon = None
            return(temp)
        else:
            print("No pokemons to release!", file=sys.stderr) # Check also : sys.stderr.write("No pokemons to release!\n")
            return(None)

