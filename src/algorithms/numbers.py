
'''
Title: fibonacci
Complexity: O(n)

Description:
    The Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
    In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 
    Fn = Fn-1 + Fn-2

    with seed values  
    F0 = 0 and F1 = 1.
'''
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    