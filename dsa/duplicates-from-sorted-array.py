##### Brute Force Approach #####

def removeDuplicates(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i+=1
        
    return nums

nums = [1, 1, 2, 2, 3, 4, 4, 5]

print(removeDuplicates(nums),'and length ==>',len(nums))

##### Time complexity is O(n^2) because of loop plus pop operation