from utils import swap, test_sorting

def selection_sort(a):
    i = len(a) - 1
    while i > 0:
        j = i - 1
        while j >= 0:
            if a[j] > a[i]:
                swap(a, j, i)
            j -= 1
        i -= 1

def main():
    test_sorting(selection_sort, returns_sorted=False)

if __name__ == '__main__':
    main()
