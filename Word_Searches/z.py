from func import s_vertical
from func import horiz_to_vert

def main():
#    grid = [] # A SUPPR
    f = open("grid")
    grid_line = f.read()
    f.close()
    f = open("words.dic")
    words = f.read().split('\n')
    f.close()

    words = s_vertical(words, grid_line)
    words = s_vertical(words, grid_line[::-1])
    words = s_vertical(words, horiz_to_vert(grid_line))
    words = s_vertical(words, horiz_to_vert(grid_line[::-1]))
    
    print(words)

if __name__ == "__main__":
    main()
