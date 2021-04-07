from math import sqrt

from .number import fibonacci


'''
Title: linear_search
Complexity: O(n)

Descripion:
    A simple approach is to do a linear search, i.e  

    Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
    If x matches with an element, return the index.
    If x doesn’t match with any of elements, return -1.
'''
def linear_search(arr, y, lower=None, upper=None):
    if not lower:
        lower = 0
    if not upper:
        upper = len(arr)
    for i in range(lower, upper):
        if arr[i] == y:
            return i 
    return -1


'''
Title: binary_search
Complexity: O(log n)

Description:
    Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. 
    If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. 
    Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.
'''
def binary_search(arr, y, lower=None, upper=None):
    if not lower:
        lower = 0
    if not upper:
        upper = len(arr) - 1
    
    while lower <= upper:
        mid = lower + (upper - lower) // 2
        # Check if x is present at mid
        if arr[mid] == y:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < y:
            lower = mid + 1
        # If x is smaller, ignore right half
        else:
            upper = mid - 1
    # If we reach here, then the element
    # was not present
    return -1

def binary_search_recursive(arr, y, lower=None, upper=None):
    if not lower:
        lower = 0
    if not upper:
        upper = len(arr) - 1

    return _binary_search_recursive(arr, y, lower, upper)

def _binary_search_recursive(arr, y, lower, upper):
    if upper >= lower: 
        mid = lower + (upper - lower) // 2
        
        if arr[mid] == y:
            return mid
        
        elif arr[mid] < y:
            return _binary_search_recursive(arr, y, mid+1, upper)
        else:
            return _binary_search_recursive(arr, y, lower, mid-1)
    else:
        return -1

'''
Title: jump_start
Complexity: O(√n)

Description:
    The basic idea is to check fewer elements by jumping ahead by fixed steps or skipping some 
    elements in place of searching all elements.
'''
def jump_search(arr, y, step=None):
    if not step:
        # Finding block size to be jumped
        step = sqrt(len(arr))
    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while arr[int(min(step, len(arr)) - 1)] < y:
        prev = step
        step += sqrt(len(arr))
        if prev >= len(arr):
            return -1
    # Doing a linear search for y in
    # block beginning with prev.
    return linear_search(arr, y, lower=int(prev))


'''
Title: interpolation_search
Complexity: O(log2(log2 n))

Description:
    The Interpolation Search is an improvement over Binary Search for instances, where the values in a sorted array are uniformly distributed. 
    Binary Search always goes to the middle element to check. On the other hand, interpolation search may go to different locations according to the value of the key being searched.

    Step1: In a loop, calculate the value of “pos” using the probe position formula. 
    Step2: If it is a match, return the index of the item, and exit. 
    Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array. Otherwise calculate the same in the right sub-array. 
    Step4: Repeat until a match is found or the sub-array reduces to zero.
'''
def interpolation_search(arr, y, lower=None, upper=None):
    if not lower:
        lower = 0
    if not upper:
        upper = len(arr) - 1
    
    return _interpolation_search(arr, y, lower, upper)

def _interpolation_search(arr, y, lower, upper):
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    if (lower <= upper and y >= arr[lower] and y <= arr[upper]):
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lower + ((upper-lower) // (arr[upper]-arr[lower]) * (y-arr[lower]))

        # Condition of target found
        if arr[pos] == y:
            return pos
        # If x is larger, x is in right subarray
        if arr[pos] < y:
            return _interpolation_search(arr, y, pos + 1, upper)
        # If x is smaller, x is in left subarray
        if arr[pos] > y:
            return _interpolation_search(arr, y, lower, pos - 1)
    return -1

'''
Title: exponential_search
Complexity: O(log n)

Description:
    The idea is to start with subarray size 1, compare its last element with x, then try size 2, 
    then 4 and so on until last element of a subarray is not greater. 
    Once we find an index i (after repeated doubling of i), 
    we know that the element must be present between i/2 and i (Why i/2? because we could not find a greater value in previous iteration)
'''
def exponential_search(arr, y):
    # IF x is present at first
    # location itself
    if arr[0] == y:
        return 0
    # Find range for binary search
    # i by repeated doubling
    i = 1
    while i < len(arr) and arr[i] <= y:
        i = i * 2
    # Call binary search for the found range
    return binary_search_recursive(arr, y, lower=i//2, upper=min(i, len(arr)-1))


'''
Title: fibonacci_search
Complexity: O(log n)

Description:
    The idea is to first find the smallest Fibonacci number that is greater than or equal to the length of the given array. 
    Let the found Fibonacci number be fib (m’th Fibonacci number). We use (m-2)’th Fibonacci number as the index (If it is a valid index). 
    Let (m-2)’th Fibonacci Number be i, we compare arr[i] with x, if x is same, we return i. Else if x is greater, we recur for subarray after i, 
    else we recur for subarray before i.
'''
def fibonacci_search(arr, y):
    # find smallest fibonacci number greater or equal
    # to the length of the arr
    pos = 0
    while (fib := fibonacci(pos)) < len(arr):
        pos += 1
    # Marks the eliminated range from front
    offset = -1

    fib2 = fibonacci(pos-2)
    fib1 = fibonacci(pos-1)

    # while there are elements to be inspected.
    # Note that we compare arr[fib2] with y.
    # When fib becomes 1, fibMm2 becomes 0
    while fib > 1:
        # check i fib2 is a valid index
        i = min(offset + fib2, len(arr)-1)
        # element found. return index
        if arr[i] == y:
            return i
        # If y is greater than the value at
        # index fib2, cut the subarray array
        # from offset to i
        elif arr[i] < y:
            fib = fib1
            fib1 = fib2  
            fib2 = fib - fib1
            offset = i
        # If y is less than the value at
        # index fib2, cut the subarray
        # after i+1
        else:
            fib = fib2
            fib1 = fib1 - fib2  
            fib2 = fib - fib1
    # comparing the last element with y
    if fib1 and arr[-1] == y:
        return len(arr) - 1
    # element not found. return -1
    return -1


'''
Title: ternary_search
Complexity: O(log3 n)

Description:
    Ternary search is a divide and conquer algorithm that can be used to find an element in an array. 
    It is similar to binary search where we divide the array into two parts but in this algorithm, 
    we divide the given array into three parts and determine which has the key.
'''
def ternary_search(arr, y, lower=None, upper=None):
    if not lower:
        lower = 0
    if not upper:
        upper = len(arr) - 1

    while upper >= lower:
        # Find mid1 and mid2
        mid1 = lower + (upper-lower)//3 
        mid2 = upper - (upper-lower)//3 
        # Check if key is at any mid
        if arr[mid1] == y:
            return mid1
        if arr[mid2] == y:
            return mid2
        # Since key is not present at mid,
        # Check in which region it is present
        # Then repeat the search operation in that region
        if arr[mid1] > y:
            # key lies between lower and mid1
            upper = mid1 - 1
        elif arr[mid2] < y:
            # key lies between mid2 and upper
            lower = mid2 + 1
        else:
            # key lies between mid1 and mid2
            lower = mid1 + 1
            upper = mid2 - 1
    # key not found
    return -1

def ternary_search_recursive(arr, y):
    return _ternary_search_recursive(arr, y, 0, len(arr)-1)

def _ternary_search_recursive(arr, y, lower, upper):
    if upper >= lower:
        # Find mid1 and mid2
        mid1 = lower + (upper-lower)//3 
        mid2 = upper - (upper-lower)//3 
        # Check if key is at any mid
        if arr[mid1] == y:
            return mid1
        if arr[mid2] == y:
            return mid2
        # Since key is not present at mid,
        # Check in which region it is present
        # Then repeat the search operation in that region
        if arr[mid1] > y:
            # key lies between lower and mid1
            return _ternary_search_recursive(arr, y, lower, mid1 - 1)
        elif arr[mid2] < y:
            # key lies between mid2 and upper
            return _ternary_search_recursive(arr, y, mid2 + 1, upper)
        else:
            # key lies between mid1 and mid2
            return _ternary_search_recursive(arr, y, mid1 + 1, mid2 - 1)
    # Key not found
    return -1
