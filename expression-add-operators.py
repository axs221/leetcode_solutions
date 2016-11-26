# https://leetcode.com/problems/expression-add-operators/

import itertools

class Solution(object):
    def __init__(self):
        self.operators = ["+", "-", "*"]

    def getAllFormulas(self, nums):
        print "nums: %s" % (nums)
        if len(nums) == 0:
            return []

        nums_with_operators = [[p + o for o in self.operators] for p in nums[:-1]] + [[nums[-1]]]
        combinations = list(itertools.product(*nums_with_operators))
        formulas = [''.join(x) for x in combinations]

        return formulas

    def getNumberCombinations(self, num):
        nums = list(num)
        return [nums]

    def addOperators(self, num, target):
        solutions = []
        formulas = []

        numberCombinations = self.getNumberCombinations(num)
        for numberCombination in numberCombinations:
            formulas += self.getAllFormulas(numberCombination)

        for formula in formulas:
            if eval(formula) == target:
                solutions.append(formula)

        return solutions

if __name__ == '__main__':
    s = Solution()
    print s.addOperators("123", 6)
    # print s.addOperators("123", 15)
    # print s.addOperators("1235", 29)
    # print s.addOperators("", 5)
    # s.getAllFormulas(["1", "2", "3"])
