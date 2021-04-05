''''
Title: is_sorted.

Description:
    Check if a given array is sorted. 
    return True if sorted.
    return False if not sorted.
''''
def is_sorted(arr):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

''''
Title: bubble_sort_for. 
Complexity: O(n^2).

Description: Itterate through the array and check all pairs.
''''
def bubble_sort_original(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

def bubble_sort_optimized(arr):
    print('buble sort while')

def selection_sort():
    print('selection sort')

def insertion_sort():
    print('insertion sort')

def merge_sort():
    print('merge sort')

def quick_sort():
    print('quick sort')
