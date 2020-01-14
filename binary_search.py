import random

def binary_search(a, x):
    return bin_search(a, 0, len(a)-1, x)

def bin_search(a, l, r, x):
    if l > r:
        return None
    
    m = (l + r) // 2
    if x == a[m]:
        return m

    if x < a[m]:
        return bin_search(a, l, m-1, x)
    else:
        return bin_search(a, m+1, r, x)

def main():
    a = [random.randint(0, 60) for _ in range(10)]
    a.sort()
    print("Test list:", a)

    x = random.choice(a)
    print("Test x:", x)

    i = binary_search(a, x)
    print("x at index:", i)

    y = -10
    print("Test y:", y)

    j = binary_search(a, y)
    print("y at index:", j)

if __name__ == "__main__":
    main()
