def empty_rectangle(height, width):
    if height < 0 or width < 0:
        return (1)
    for i in range(height):
        s = ''
        for j in range(width):
            if j != 0 and j != width - 1 and i != 0 and i != height - 1:
                s += ' '
            else:
                s += '*'
        print(s)

# TODO : Check for 1/0 & 0/1
