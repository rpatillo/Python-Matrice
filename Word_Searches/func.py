# Bla
# 4 fonctions :
# Lecture verticale normal
# Lecture verticale inversée
# Lecture horizontale vers le haut
# Lecture horizontale vers le bas

def s_vertical(liste, grid):
    for i in liste:
        if i in grid:
            liste.remove(i)
    return(liste)

def horiz_to_vert(grid):
    l = grid.find('\n')
    s = ''
    k = 0
    for j in range(l): 
        for i in range(k, len(grid), l + 1):
            s += grid[i]
        k += 1
    return(s)
