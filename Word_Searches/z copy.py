
def main():
    f = open("grid")
    grid_line = f.read().split('\n')
    f.close()
    f = open("words.dic")
    words = f.read().split('\n')
    f.close()

    grid_line = search_words(grid_line, words)
    grid_line = search_words(search_vert(grid_line), words)
    grid_line = search_vert(grid_line, 1)
    print(*grid_line, sep='\n')


# Function that search words within the grid. Replacing them by uppercase. And removing words for the words list.
# Return the new list.
def search_words(grid, words):
    sgrid = []
    for i in grid:
        for j in words:
            if j.lower() in i.lower(): 
                i = i.replace(j, j.upper())
                words.remove(j)
        for j in words:
            if j.lower() in i[::-1].lower():
                i = i[::-1].replace(j, j.upper())[::-1]
                words.remove(j)
        sgrid.append(i)
    return(sgrid)

# Create a list of each column of the grid. 
# Return the new list.
# flag variable is used to handle some length problem. Should check back for a more clever soluton.
def search_vert(grid, flag=None):
    list_vert = []
    if flag == None:
        f_len = len(grid) - 1
    else:
        f_len = len(grid)
    for i in range(len(grid[0])):
        str_temp = ""  
        for j in range(f_len):
            str_temp += grid[j][i]
        list_vert.append(str_temp)
    return(list_vert)

# Draft from other version (using only strings)
# Change grid to create list of diag.
# Check for all 4 directions ( X )
def diag_sub(grid):
    l = grid.find('\n') + 1
    s = ''
    h = grid.count('\n')
    for j in range(1, h):
        print(l*j)
        for i in range(l * j, len(grid), l + 1):
            if grid[i] == '\n':
                break
            if j % 2 == 0:
                s += grid[i]
            elif j % 2 == 1:
                s += grid[i].upper()
    return(s)

if __name__ == "__main__":
    main()
