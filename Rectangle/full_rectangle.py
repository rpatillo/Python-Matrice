def full_rectangle(height, width):
    for i in range(height):
        s = ''
        for j in range(width):
            s += '*'  # print('*', end='')
        print(s) # print('')

def full_rectangle2(height, width):
    for i in range (height):
        if width > 0:
            print('*' * width)

# TODO : Check for 1/0 & 0/1
