"""
Find next greater number with same set of digits
Given a number n, find the smallest number that has same set of digits as n and is greater than n. If x is the greatest possible number with its set of digits, then print “not possible”.
Examples:
For simplicity of implementation, we have considered input number as a string.

"""
import math

def get_digit_set(number):
    s = str(number)

def get_numbers(digits):
    if len(digits) == 1:
        return [digits[0]]
    numbers = []
    for digit in digits:
        cp = digits.copy()
        cp.remove(digit)
        numbers += [digit * math.pow(10, len(cp)) + n for n in get_numbers(cp)]
    return numbers

def find_next_greater_number(number):
    digits =[int(d) for d in str(number)]
    numbers = get_numbers(digits)
    gt = [n for n in numbers if n > number]
    gt.sort()
    if len(gt) > 0:
        return gt[0]
    else:
        return "not possible"

def test_find_next_greater_number():
    number = 234500
    nxt = find_next_greater_number(number)
    print(nxt)

test_find_next_greater_number()