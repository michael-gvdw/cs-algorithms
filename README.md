# cs-algorithms

## Context
    


# Currently Implemented

## Sorting Algorithms:

### Is Sorted
    Check if a given array is sorted (works for ascending and descending order).

### Bubble Sort (Original)
    Repeatedly swapps adjacent elements if they are in wrong order. (uses two nested for loops)

[Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/bubble-sort/)

### Bubble Sort (Optimized)
    Repeatedly swapping the adjacent elements if they are in wrong order (stops when array is sorted).

[Wikipedia](https://en.wikipedia.org/wiki/Bubble_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/bubble-sort/)

### Selection Sort
    Repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. 

[Wikipedia](https://en.wikipedia.org/wiki/Selection_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/selection-sort/)

### Insertion Sort
    The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

[Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/insertion-sort/)

### Merge Sort
    It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 

[Wikipedia](https://en.wikipedia.org/wiki/Merge_sort)

[GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)

### Quick Sort
    It picks an element as pivot and partitions the given array around the picked pivot. 

[Wikipedia](https://en.wikipedia.org/wiki/Quicksort)

[GeeksforGeeks](https://www.geeksforgeeks.org/quick-sort/)

## Search Algorithms:

### Linear Search
    Start from the leftmost element of arr[] and one by one compare x with each element of arr[] If x matches with an element, return the index. If x doesn’t match with any of elements, return -1.
    
[Wikipedia](https://en.wikipedia.org/wiki/Linear_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/linear-search/)

### Binary Search (Iterative) 
    Search a sorted array by repeatedly dividing the search interval in half. Begin wiht an intreval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the intreval to the lower half. Otherwise narrow it to the upper half. Repaetadly check until the value is found or the interval is empty. 

[Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

[GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)

### Binary Search (Recursive)
    See Binary Search (Iterative).

[Wikipedia](https://en.wikipedia.org/wiki/Binary_search_algorithm)

[GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)

### Jump Search
    The basic idea is to check fewer elements by jumping ahead fixed steps or skipping some elements in place of searching all elements.

[Wikipedia](https://en.wikipedia.org/wiki/Jump_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/jump-search/)

### Interpolation Search
    The Interpolation Search is an improvement over the Binary Search for instance, where the values in a sorted array are uniformly distributed. Binary Search always goes to the middle elemnt to check. On the other hand, Interpolation Search may go to different positions according to the value of the key being searched.

[Wikipedia](https://en.wikipedia.org/wiki/Interpolation_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/interpolation-search/)

### Exponential Search
    The idea is to start with subarray size 1, compare its element with the key value, then try size 2, then try size 4 and so on until the last element of subarray is not greater. Once we find an index i, we know that the element must be present between i/2 and i.

[Wikipedia](https://en.wikipedia.org/wiki/Exponential_search)

[GeeksforGeeks](https://www.geeksforgeeks.org/exponential-search/)

### Fibonacci Search
    The idea is to find the smallest Fibonacci number that is greater than or equal to the length of the given array. Let the found Fibonacci number be fib. We can use the (m-2)'th Fibonacci number as the index. Let (m-2)'th Fibonacci number be i, we compare arr[i] with the key value. If the key value is same, we return i. Else if the key value is greater, we recur for subarray after i, else we recur for the subarray before i.

[Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_search_technique)

[GeeksforGeeks](https://www.geeksforgeeks.org/fibonacci-search/)
    
        
## Data Structures:
### Queue

### Stack

### BinaryTree

### BinarySearchTree

