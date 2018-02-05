from utils import sort_string, build_string

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

#Problem 1.3
#Write a method to replace all spaces in a string with '%20'. You may assume
#the string has sufficient space at the end to hold additional characters,
#and that you are given the true length of the string.
def urlify(w, length):
    """
    First solution uses python built-in functions
    in a simple one-liner.
    """
    return w.strip().replace(' ', '%20')

def urlify2(w, length):
    """
    Second solution walks through the string once and detects words
    and spaces, adding appropriate strings to a list. It then uses
    a StringBuilder-like method to efficiently concatenate them.
    Runs in O(n).
    """
    chars = []
    while i < len(w):
        c = w[i]
        if c == ' ':
            chars.append('%20')        
        else:
            chars.append(' ')
    url_w = build_string(chars)
    return url_w
