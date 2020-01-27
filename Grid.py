a = "abcdeXeabcdXdeabcXcdeabXbcdea"

# for i in range(0, len(a), 7):
#     print(a[i])


lo = 5 + 2 # length of line + 1 to go to the first char of newline + 1 to move to the right
for j in range (5):
    for i in range(j, len(a), lo):
        if (i == 0):
            print("0 !", a[i])
        elif ((lo + j) % i == 0):
            print(a[i], i, j)
    print('')