class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff = {}
        # output = []
        # for i in range(len(nums)):
        #     if nums[i] in diff.keys():
        #         j = diff[nums[i]]
        #         if i != j:
        #             output.append(j)
        #             output.append(i)
        #             return output
        #     else:
        #         diff[target - nums[i]] = i
            
        # # for j in range(len(nums)):
        # #     if nums[j] in diff.keys() and diff[nums[j]] != j:
        # #         output.append(diff[nums[j]])
        # #         output.append(j)
        # #         return output
        # return output
        dict_diff = {}
        for i in range(len(nums)):
            dict_diff[nums[i]] = i
        print(dict_diff)
        for j in range(len(nums)):
            if target-nums[j] in dict_diff:
                if j != dict_diff[target-nums[j]]:
                    return [dict_diff[target-nums[j]], j]
        return []