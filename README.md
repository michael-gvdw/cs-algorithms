# cs-algorithms 

## Goal
The main goal is to familiarize with common Algorithms and Data Structures. Folowing an added benefit is that this code will be accessible and re-useable. 

[Linkedin](https://www.linkedin.com/in/michael-groenewegen-van-der-weijden-4234b9206/)

## File Structure

    algorithms/
        -> number.py
        -> search.py
        -> sorting.py
        data_strucutes/
            -> sequence.py
            -> tree.py

## Instalation

    pip install cs-algorithms

# Currently Implemented

## Numbers:

### Fibonacci Sequence

The Fibonacci numbers are the numbers in the following integer sequence.

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,... 

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 

    Fn = Fn-1 + Fn-2

with seed values  

    F0 = 0 and F1 = 1.

#### Code Example

    >>> from algorithms.numbers import fibonacci

    >>> fib = fibonacci(10)
    >>> print(fib)

    output: 34

### Factorial

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n:

    n!=n * (n-1) * (n-2) * (n-3) ... * 3 * 2 * 1

For example,
    
    5!=5 * 4 * 3 * 2 * 1 = 120

#### Code Example

    >>> from algorithms.numbers import factorial

    >>> fc = factorial(5)
    >>> print(fc)

    output: 120

## Sorting Algorithms:

### Is Sorted
Check if a given array is sorted (works for ascending and descending order).

#### Code Example

    >>> from algorithms.sorting import is_sorted

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> val = is_sorted(arr)
    >>> print(val)

    output: True

### Bubble Sort (Original)
Repeatedly swapps adjacent elements if they are in wrong order. (uses two nested for loops)

#### Code Example

    >>> from algoritms.sorting import bubble_sort_original

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> bubble_sort_original(arr)
    >>> print(arr)

    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

[Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/bubble-sort/)

### Bubble Sort (Optimized)
Repeatedly swapping the adjacent elements if they are in wrong order (stops when array is sorted).

#### Code Example

    >>> from algoritms.sorting import bubble_sort_optimized

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> bubble_sort_optimized(arr)
    >>> print(arr)

    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

[Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/bubble-sort/)

### Selection Sort
Repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. 

#### Code Example

    >>> from algoritms.sorting import selection_sort

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> selection_sort(arr)
    >>> print(arr)

    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

[Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/selection-sort/)

### Insertion Sort
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

#### Code Example

    >>> from algoritms.sorting import insertion_sort

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> insertion_sort(arr)
    >>> print(arr)

    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

[Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/insertion-sort/)

### Merge Sort
It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 

#### Code Example

    >>> from algoritms.sorting import merge_sort

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> merge_sort(arr)
    >>> print(arr)

    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

[Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)

### Quick Sort
It picks an element as pivot and partitions the given array around the picked pivot. 

#### Code Example

    >>> from algoritms.sorting import quick_sort

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> quick_sort(arr)
    >>> print(arr)

    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


[Wikipedia](https://en.wikipedia.org/wiki/Quicksort)

[GeeksforGeeks](https://www.geeksforgeeks.org/quick-sort/)

### Binary Insertion Sort
Binary Insertion Sort uses binary search to find the proper location to insert the selected item at each iteration.

#### Code Example

    >>> from algorithms.sorting import binary_insertion_sort

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> arr = binary_insertion_sort(arr)
    >>> print(arr)

    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Search Algorithms:

### Linear Search
Start from the leftmost element of arr[] and one by one compare x with each element of arr[] If x matches with an element, return the index. If x doesn’t match with any of elements, return -1.

#### Code Example 

    >>> from algoritms.search import linear_search

    >>> arr = [5, 2, 3, 6, 1, 4, 8, 9, 7]
    >>> index = linear_search(arr, 6)
    >>> print(index)

    output: 3
    
[Wikipedia](https://en.wikipedia.org/wiki/Linear_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/linear-search/)

### Binary Search (Iterative) 
Search a sorted array by repeatedly dividing the search interval in half. Begin wiht an intreval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the intreval to the lower half. Otherwise narrow it to the upper half. Repaetadly check until the value is found or the interval is empty. 

#### Code Example

    >>> from algoritms.search import binary_search

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = binary_rearch(arr, 6)
    >>> print(index)

    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

[GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)

### Binary Search (Recursive)
See [Binary Search (Iterative)](###binary-search-(iterative)).

#### Code Example

    >>> from algoritms.search import binary_search_recursive

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = binary_search_recursive(arr, 6)
    >>> print(index)

    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

[GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)

### Jump Search
The basic idea is to check fewer elements by jumping ahead fixed steps or skipping some elements in place of searching all elements.

#### Code Example

    >>> from algorithms.search import jump_search

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = jump_search(arr, 6)
    >>> print(index)

    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Jump_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/jump-search/)

### Interpolation Search
The Interpolation Search is an improvement over the Binary Search for instance, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle elemnt to check. On the other hand, Interpolation Search may go to different positions according to the value of the key being searched.

#### Code Example

    >>> from algoritms.search import interpolation_search

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = interpolation_search(arr, 6)
    >>> print(index)

    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Interpolation_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/interpolation-search/)

### Exponential Search
The idea is to start with subarray size 1, compare its element with the key value, then try size 2, then try size 4 and so on until the last element of subarray is not greater. Once we find an index i, we know that the element must be present between i/2 and i.

#### Code Example

    >>> from algorithms.search import exponential_search

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = exponential_search(arr, 6)
    >>> print(index)

    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Exponential_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/exponential-search/)

### Fibonacci Search
The idea is to find the smallest Fibonacci number that is greater than or equal to the length of the given array. Let the found Fibonacci number be fib. We can use the (m-2)'th Fibonacci number as the index. Let (m-2)'th Fibonacci number be i, we compare arr[i] with the key value. If the key value is same, we return i. Else if the key value is greater, we recur for subarray after i, else we recur for the subarray before i.

#### Code Example

    >>> from algoritms.search import fibonacci_search

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = fibonacci_search(arr, 6)
    >>> print(index)
    
    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_search_technique)

[GeeksforGeeks](https://www.geeksforgeeks.org/fibonacci-search/)
    
### Ternary Search (Iterative)
Ternary search is a divide and conquer algorithm that can be used to find an element in an array. It is similar to binary search where we divide the array into two parts but in this algorithm, we divide the given array into three parts and determine which has the key.

#### Code Example

    >>> from algorithms.search import ternary_search

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = ternary_search(arr, 6)
    >>> print(index)

    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/ternary-search/#:~:text=Ternary%20search%20is%20a%20divide,the%20key%20(searched%20element).)

### Ternary Search (Recursive)
See [Ternary Search (Iterative)](###ternary-search-(iterative)).

#### Code Example

    >>> from algorithms.search import ternary_search_recursive

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> index = ternary_search_recursive(arr, 6)
    >>> print(index)

    output: 5

[Wikipedia](https://en.wikipedia.org/wiki/Ternary_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/ternary-search/#:~:text=Ternary%20search%20is%20a%20divide,the%20key%20(searched%20element).)
        
## Data Structures:

### Queue

### Stack

### Binary Tree

### Binary Search Tree

