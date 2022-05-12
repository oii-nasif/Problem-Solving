class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i, n in enumerate(nums):
            num_target = target - n
            if num_target in num_dict:
                return [i, num_dict[num_target]]
            num_dict[n] = i 
            