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
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Quick sort
def quick_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Merge sort
def merge_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Heap sort
def heap_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Radix sort (LSD)
def radixLSD_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Radix sort (MSD)
def radixMSD_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#gcc std::sort
def gcc_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#gcc std::stable_sort
def gcc_stable_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Shell sort
def shell_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Bubble sort
def bubble_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Cocktail sort
def cocktail_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Gnome sort
def gnome_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Optimized Gnome sort
def gnome_optimized_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Bitonic sort
def bitonic_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Bogo sort
def bogo_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Comb sort
def comb_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
#Pigeonhole
def pigeonhole_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")