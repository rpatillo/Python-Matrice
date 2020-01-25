def full_rectangle(height, width):
    for i in range(height):
        s = ''
        for j in range(width):
            s += '*'
            #print('*', end='')
        print(s)

# Todo : Concatenate string : string += '*' ?

H = int(input("Height :"))
W = int(input("Width :"))
full_rectangle(H, W)