#---Imports
from logging import exception
import math

#---Usefultools
def swap(arr,i,j):
    if type(arr) is not list or type(i) is not int or type(j) is not int:
        raise Exception("Invalid parameter given")
    arr[i], arr[j] = arr[j], arr[i]

#---Selection sort
def selection_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
    for idx in range(len(arr)):
        x = idx
        for i in range(idx,len(arr)):
            if arr[i] < arr[x]:
                x = i
        swap(arr,x,idx)
    return arr

#---Insertion sort
def insertion_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
    for idx in range(1,len(arr)):
        x = 0
        if arr[idx] < arr[idx - 1] and x > 0:
            x = idx
            while arr[x] < arr[x-1]:
                swap(arr, x, (x-1))
                x -= 1
    return arr

#---Quick sort
def quick_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")
    def part(a, b, t):
        pi = a[t]
        p = b - 1
        for i in range(b, t):
            if a[i] > pi:
                continue
            p += 1
            swap(a, p, i)
        swap(a, (p+1), t)
        return p + 1
    def sort(a, b, t):
        if b > t:
            return  1
        pi = part(a, b, t)
        sort(a, b, (pi-1))
        sort(a, (pi+1), t)
    sort(arr, 0, (len(arr) - 1))
    return arr

#---Merge sort
def merge_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Heap sort
def heap_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Radix sort (LSD)
def radixLSD_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Radix sort (MSD)
def radixMSD_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---gcc std::sort
def gcc_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---gcc std::stable_sort
def gcc_stable_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Shell sort
def shell_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Bubble sort
def bubble_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Cocktail sort
def cocktail_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Gnome sort
def gnome_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Optimized Gnome sort
def gnome_optimized_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Bitonic sort
def bitonic_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Bogo sort
def bogo_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Comb sort
def comb_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")

#---Pigeonhole
def pigeonhole_sort(arr):
    if type(arr) is not list:
        raise Exception("Parameter must be a list")