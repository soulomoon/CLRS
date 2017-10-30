"""
Consider sorting n numbers stored in array A by first finding the smallest element
of A and exchanging it with the element in AOE1". Then find the second smallest
element of A, and exchange itwith AOE2". Continue in thismanner for the first n$1
elements of A. Write pseudocode for this algorithm, which is known as selection
sort. What loop invariant does this algorithm maintain? Why does it need to run
for only the first n $ 1 elements, rather than for all n elements? Give the best-case
and worst-case running times of selection sort in ‚-notation.
"""


def selection_sort(l):
    for i in range(len(l)-1):
        temp_index = None
        for j in range(i, len(l)):
            if temp_index == None or l[temp_index ]> l[j]:
                temp_index = j
        temp = l[temp_index]
        l[temp_index] = l[i]
        l[i] = temp
    return l


### What loop invariant does this algorithm maintain?
"The loop (l[0]..l[i]) is the loop invariant"
### why does it need to run for only the first n-1 elements ranther than for
### n elements?
"Because for all the time, number in loop invariant is always smaller than the \
    rest"
### Give the best-case and worst-case running times of selection sort in ‚-notation.
"Best case is the same as the worst case O(n^2)"

