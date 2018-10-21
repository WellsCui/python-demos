class Solution:
    def sortedInsert(self, ls, element):
        high = len(ls)
        low = 0
        while high > low:
            half = low + (high - low) // 2
            if ls[half] == element:
                return ls[:half] + [element] + ls[half:]
            elif ls[half] > element:
                high = half - 1
            else:
                low = half + 1
        return ls[:high] + [element] + ls[high:]

    def sortedInsertWithSize(self, ls, element, size):
        if len(ls) == size:
            if ls[0] >= element:
                return ls
            else:
                ls.pop(0)
                return self.sortedInsert(ls, element)
        else:
            return self.sortedInsert(ls, element)

    def find(self, lst, n):
        rs = []
        for item in lst:
            rs = self.sortedInsertWithSize(rs, item, n)
        return rs


result = Solution().find([3,6,7,8,8,9,2,4,5,6,6,7], 5)
for r in result:
    print(r)
