from utils import test_sorting, swap

def insertion_sort(a):
    i = 0
    while i < len(a) - 1:
        j = i + 1
        while j > 0 and a[j] < a[j-1]:
            swap(a, j-1, j)
            j -= 1
        i += 1

def main():
    test_sorting(insertion_sort, returns_sorted=False)

if __name__ == '__main__':
    main()
