from empty_rectangle import empty_rectangle as e_rect
from full_rectangle import full_rectangle as f_rect

def pattern(mlist, height, width):
    for i in mlist:
        if i == "empty":
            e_rect(height, width)
        elif i == "full":
            f_rect(height, width)

# TEST :
# wrd = input("List of words :").split()
# h, w = input("Height Width :").split()
# pattern(wrd, int(h), int(w))
