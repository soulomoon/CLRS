# 2.1-3
# Consider the searching problem:
# Input: A sequence of n numbers A D ha1;a2;:::;ani and a value  .
# Output: An index i such that   D AŒi  or the special value NIL if   does not
# appear in A.
# Write pseudocode for linear search, which scans through the sequence, looking for  . Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.


def search(a_list, v):
    for index, n in enumerate(a_list):
        if n == v:
            return index
    return False
