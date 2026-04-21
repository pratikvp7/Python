
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        This is O(n^2)
        """
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index1 == index2:
                    break
                sum_of = num1 + num2
                if sum_of == target:
                    return [index2, index1]
        raise Exception("No sum matches the target value.")
    
    def two_sum_sol2(self, nums, target):
        """
        This is O(n) - better approach
        """
        seen = {}
        for index, num in enumerate(nums):
            num2 = target - num

            if num2 in seen:
                return [seen[num2], index]
            
            seen[num] = index
        raise Exception("No sum matches the target value.")
            

    


if __name__ == "__main__":
    sol = Solution()
    indices = sol.two_sum(nums=[8, 2, 7], target=9)
    print(indices)

    indices = sol.two_sum_sol2(nums=[8, 2, 7], target=9)
    print(indices)


