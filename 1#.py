"""
Task

Given a binary number, we are about to do some operations on the number. Two types of operations can be here:

    ['I', i, j] : Which means invert the bit from i to j (inclusive).

    ['Q', i] : Answer whether the i'th bit is 0 or 1.

The MSB (most significant bit) is the first bit (i.e. i = 1). The binary number can contain leading zeroes.
"""

def binary_simulation(s, q):
    res=[]
    for i in q:
        if i[0] == 'I':
            s = s[:i[1]-1] + revert(s[i[1] - 1:i[2]]) + s[i[2]:]
        if i[0] == 'Q':
            res.append(s[i[1]-1])
    print(res)


def revert(string):
    new_string = ''
    for i in string:
        if i == '0':
            new_string += '1'
        else:
            new_string += "0"
    return new_string


binary_simulation("0011001100", [['I', 1, 10],['I', 2, 7], ['Q', 2], ['Q', 1], ['Q', 7], ['Q', 5]])
#[['I', 1, 10],