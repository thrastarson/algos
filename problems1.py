from utils import sort_string

#Problem 1.1
#Implement an algorithm to determine if a string has all unique characters.
#What if you cannot use an external data structure?
def is_unique(w):
    """
    First solution uses a dictionary or hash table
    to record previously unseen characters in w.
    Runs in O(n).
    """
    chars = {}
    for c in w:
        if c in w:
            return False
        chars[c] = True
    return True

def is_unique2(w):
    """
    Second solution sorts w and scans to see if any
    adjacent characters are the same.
    Runs in O(n*log(n)).
    """
    if len(w) <= 1:
        return True

    w_sorted = sort_string(w)
    i = 0
    while i < len(w_sorted) - 1:
        if w_sorted[i] == w_sorted[j]:
            return False
        i += 1
    return True

