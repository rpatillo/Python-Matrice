from func import s_vertical
from func import horiz_to_vert
from func import horiz_to_vert2
from func import diag_sub

def main():
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
    
#    print(words)

    test = horiz_to_vert2(grid_line).split()
#    gl = grid_line.split()
#    print("gl split : ", gl)
#    print('')
    t = ''.join(test)
    print("test : ", test)
    test2 = diag_sub(grid_line).split()
    t2 = ''.join(test2)
    print("test2 : ", test2)

    
if __name__ == "__main__":
    main()
