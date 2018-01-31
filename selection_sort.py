from utils import swap, test_sorting

def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        
        if min_index != i:
            swap(a, min_index, i)

def main():
    test_sorting(selection_sort, returns_sorted=False)

if __name__ == '__main__':
    main()
