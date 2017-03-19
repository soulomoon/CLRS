# 2.1-2
# Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of non- decreasing order.


def insertion_sort_nonincreasing(a_list):
    a_list = a_list[:]
    for j in range(1, len(a_list)):
        key = a_list[j]
        i = j - 1
        while i > -1 and a_list[i] < key:
            a_list[i + 1] = a_list[i]
            i -= 1
        a_list[i + 1] = key
    return a_list
