# https://leetcode.com/problems/expression-add-operators/

import itertools

class Solution(object):
    def __init__(self):
        self.operators = ["+", "-", "*"]

    def getAllFormulas(self, nums):
        if len(nums) == 0:
            return []
        elif type(nums) is not list:
            return [nums]

        nums_with_operators = [[p + o for o in self.operators] for p in nums[:-1]] + [[nums[-1]]]
        combinations = list(itertools.product(*nums_with_operators))
        formulas = [''.join(x) for x in combinations]

        return formulas

    def flatten(self, possibly_nested_list):
        if len(possibly_nested_list) > 0 and type(possibly_nested_list[0]) is list:
            return list(itertools.chain(*possibly_nested_list))
        else:
            return possibly_nested_list

    def getNumberCombinations(self, nums):
        allCombinations = []

        for i in range(len(nums)):
            num = ''.join(nums[:i+1])
            other_nums = nums[i+1:]
            combinations = self.getNumberCombinations(other_nums)

            combined = []
            if len(combinations) > 0:
                combined = [[num] + self.flatten(combo) for combo in combinations]
            else:
                combined = [num]

            if len(num) == 1 or num[0] != '0':  # LeetCode solution doesn't consider 1*05 = 5 as an acceptable answer
                allCombinations.append(combined)

        return allCombinations

    def addOperators(self, num, target):
        solutions = []
        all_formulas = []

        nums = list(num)
        numberCombinations = self.flatten(self.getNumberCombinations(nums))

        for numberCombination in numberCombinations:
            formulas = self.getAllFormulas(numberCombination)
            all_formulas += formulas

        for formula in all_formulas:
            if eval(formula) == target:
                solutions.append(formula)

        return solutions

if __name__ == '__main__':
    s = Solution()
    print "--------------------------------------------------------------------------------------------------------"
    # print "123, 123:", s.addOperators("123", 123)
    # print "123, 6:", s.addOperators("123", 6)
    print "105, 5:", s.addOperators("105", 5)
    # print "123, 15:", s.addOperators("123", 15)
    # print "1235, 29:", s.addOperators("1235", 29)
    # print "[], 5:", s.addOperators("", 5)
