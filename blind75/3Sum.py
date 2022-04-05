# https://leetcode.com/problems/3sum/


# use three pointers
# must sort the list first
# weird egde cases
# be sure to understand 

def three_sum(nums):
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]

            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                # also check for duplicates
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    
    return res