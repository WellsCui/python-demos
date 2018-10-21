# An array containing heights of building was given.
# Its a rainy season. Calculate the amount of water collected between all the buildings.

class Solution:

    def calculate_bar(self, left, middle, right):
        if left <= middle or middle >= right:
            return 0
        else:
            return min(left, right)-middle

    def calculate(self, heights):
        size = len(heights)
        if size < 3:
            return 0
        left_bars = []
        right_bars = []
        left_max = heights[0]
        for item in heights:
            if left_max > item:
                left_bars.append(left_max)
            else:
                left_bars.append(item)
                left_max = item
        right_max = heights[size-1]


        for i in range(size-1, -1, -1):
            if right_max > heights[i]:
                right_bars.insert(0, right_max)
            else:
                right_bars.insert(0, heights[i])
                right_max = heights[i]
        rs = 0
        for i in range(size):
            rs += self.calculate_bar(left_bars[i], heights[i], right_bars[i])
        return rs

def test_solution():
    print(Solution().calculate([1, 5, 3, 7, 4, 2]))

test_solution()


