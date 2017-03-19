# 2.1-4
# Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in
# an .n C 1/-element array C . State the problem formally and write pseudocode for adding the two integers.


def add_binary(a, b):
    if len(a) != len(b):
        return

    def add(x, y):
        return (x + y) % 2

    def add_with_carry(x, y, carry):
        return (add(x, y) + carry) % 2

    def get_carry(x, y, carry):
        return (x + y + carry) // 2

    c = [0 for i in range(len(a) + 1)]
    carry_bit = 0

    for index in range(len(a)-1, -1, -1):
        c[index + 1] = add_with_carry(a[index], b[index], carry_bit)
        carry_bit = get_carry(a[index], b[index], carry_bit)

    c[0] = carry_bit
    return c
