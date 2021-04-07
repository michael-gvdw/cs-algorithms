from .search import binary_search_recursive

'''
Title: is_sorted.
Complexity: O(n)

Description:
    Check if a given array is sorted. 
    return True if sorted.
    return False if not sorted.
'''
def is_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] < arr[-1]:
        return all([arr[i-1] <= arr[i] for i in range(1, len(arr))])
    return all([arr[i-1] >= arr[i] for i in range(1, len(arr))])


'''
Title: bubble_sort_original. 
Complexity: O(n^2).

Description: 
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
'''
def bubble_sort_original(arr):
    if is_sorted(arr):
        return
    # Traverse through all array elements
    for i in range(len(arr)):
        # Last i elements are already in place
        for j in range(1, len(arr)-i):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]


'''
Title: bubble_sort_optimized. 
Complexity: O(n^2).

Description: 
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
'''
def bubble_sort_optimized(arr):
    if is_sorted(arr):
        return
    swapped = False
    # Traverse through all array elements
    i = 0 
    while not swapped and i < len(arr):
        swapped = True        
        # Last i elements are already in place
        for j in range(1, len(arr) - i):
            # traverse the array from 0 to
            # n-i-1. Swap if the element 
            # found is greater than the
            # next element
            if arr[j-1] > arr[j]:
                swapped = False
                arr[j-1], arr[j] = arr[j], arr[j-1]
        i += 1


'''
Title: selection_sort. 
Complexity: O(n^2).

Description: 
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. 
    The algorithm maintains two subarrays in a given array.

    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.

    In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
'''
def selection_sort(arr):
    if is_sorted(arr):
        return
    # Traverse through all array elements
    for i in range(1, len(arr)):
        # Find the minimum element in remaining unsorted array
        index_min = i-1
        for j in range(i, len(arr)):
            if arr[index_min] > arr[j]:
                index_min = j
        # Swap the found minimum element with the first element    
        arr[i-1], arr[index_min] = arr[index_min], arr[i-1]


'''
Title: insertion_sort
Complexity: O(n*2) 

Description:
    Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 
    The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
    
    Algorithm 
    To sort an array of size n in ascending order: 
    1: Iterate from arr[1] to arr[n] over the array. 
    2: Compare the current element (key) to its predecessor. 
    3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
'''
def insertion_sort(arr):
    if is_sorted(arr):
        return
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


'''
Title: merge_sort
Complexity: O(n*log n)

Description:
    Like QuickSort, Merge Sort is a Divide and Conquer algorithm. 
    It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
'''
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements into 2 halves
        left = arr[:mid]
        right= arr[mid:]

        # Sorting the left half
        merge_sort(left)

        # Sorting the right half
        merge_sort(right)

        i = j = k = 0
        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        # Checking if any element is left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


'''
Title: quick_sort.
Complexity: O(n log n)

Description:
    Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. 
    There are many different versions of quickSort that pick pivot in different ways. 

    Always pick first element as pivot.
    Always pick last element as pivot (implemented below)
    Pick a random element as pivot.
    Pick median as pivot.

    The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. 
    All this should be done in linear time. 
'''
def quick_sort(arr):
    if is_sorted(arr):
        return
    _quick_sort(arr, low=0, high=len(arr)-1)

def _partition(arr, low, high):
    i = (low-1)  # index of smaller element
    pivot = arr[high]  # pivot
  
    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def _quick_sort(arr, low, high):
    if low < high:
        # partition_index is partitioning index, arr[partition_index] is now at right place
        partition_index = _partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        _quick_sort(arr, low, partition_index-1)
        _quick_sort(arr, partition_index+1, high)


'''
Title: binary_insertion_sort
Complexity: O(log n)

Description: 
    Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration. 
'''
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = _binary_search_insertion_sort(arr, key, lower=0, upper=i-1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    return arr

def _binary_search_insertion_sort(arr, y, lower, upper):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if lower == upper:
        if arr[lower] > y:
            return lower
        else:
            return lower+1
  
    # this occurs if we are moving beyond left\'s boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if lower > upper:
        return lower
  
    mid = (lower+upper)//2
    if arr[mid] < y:
        return _binary_search_insertion_sort(arr, y, mid+1, upper)
    elif arr[mid] > y:
        return _binary_search_insertion_sort(arr, y, lower, mid-1)
    else:
        return mid
