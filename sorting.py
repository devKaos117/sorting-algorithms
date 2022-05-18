from logging import exception
#Selection sort
def selection_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
    for idx in range(len(arr)):
        x = idx
        for i in range(idx,len(arr)):
            if arr[i] < arr[x]:
                x = i
        arr[x], arr[idx] = arr[idx], arr[x]
    return arr
#Insertion sort
def insertion_sort(arr):
    pass
#Quick sort
def quick_sort(arr):
    pass
#Merge sort
def merge_sort(arr):
    pass
#Heap sort
def heap_sort(arr):
    pass
#Radix sort (LSD)
def radixLSD_sort(arr):
    pass
#Radix sort (MSD)
def radixMSD_sort(arr):
    pass
#gcc std::sort
def gcc_sort(arr):
    pass
#gcc std::stable_sort
def gcc_stable_sort(arr):
    pass
#Shell sort
def shell_sort(arr):
    pass
#Bubble sort
def bubble_sort(arr):
    pass
#Cocktail sort
def cocktail_sort(arr):
    pass
#Gnome sort
def gnome_sort(arr):
    pass
#Optimized Gnome sort
def gnome_optimized_sort(arr):
    pass
#Bitonic sort
def bitonic_sort(arr):
    pass
#Bogo sort
def bogo_sort(arr):
    pass
#Comb sort
def comb_sort(arr):
    pass
#Pigeonhole
def pigeonhole_sort(arr):
    pass