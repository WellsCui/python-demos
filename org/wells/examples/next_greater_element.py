# Next Greater Element
# 2.9
# Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.
#
# Examples:
# a) For any array, rightmost element always has next greater element as -1.
# b) For an array which is sorted in decreasing order, all elements have next greater element as -1.
# c) For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.

import unittest


def next_greater_element(elements):
    rs = []
    unresolved_elements = []
    for i in range(len(elements)):
        rs.append(-1)
        new_unresolved_elements = []
        for j in unresolved_elements:
            if elements[j] < elements[i]:
                rs[j] = elements[i]
            else:
                new_unresolved_elements.append(j)
        unresolved_elements = new_unresolved_elements

        unresolved_elements.append(i)
    return rs


class NextGreaterElement(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(next_greater_element([4, 5, 2, 25]), [5, 25, 25, -1])
        self.assertEqual(next_greater_element([13, 7, 6, 12]), [-1, 12, 12, -1])


if __name__ == '__main__':
    unittest.main()
