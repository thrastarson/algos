def is_sorted(a):
    return a == sorted(a)

def switch(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def test_sorting(sort_foo, returns_sorted=True):
    a = [5, 4, 7, 1, 3, 2, 8, 6, 9]
    b = []
    c = [14]
    d = [5, 6, 7, 8]
    cases = [a, b, c, d]

    if returns_sorted:
        for _list in cases:
            sorted_list = sort_foo(_list)
            print(is_sorted(sorted_list), sorted_list)
    else:
        for _list in cases:
            sort_foo(_list)
            print(is_sorted(_list), _list)

