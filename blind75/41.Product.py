#  https://leetcode.com/problems/product-of-array-except-self/submissions/

# go through the list forwards finding the number multiplied forwards
# then go through backwards finding 
def productExceptSelf(nums):
        
    result = [1] * len(nums)
    
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    post = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= post
        post *= nums[i]
    
    return result