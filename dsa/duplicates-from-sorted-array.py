##### Brute Force Approach #####

# def removeDuplicates(nums):
#     i = 0
#     while i < len(nums)-1:
#         if nums[i] == nums[i+1]:
#             nums.pop(i)
#         else:
#             i+=1
        
#     return nums

# nums = [1, 1, 2, 2, 3, 4, 4, 5]

# print(removeDuplicates(nums),'and length ==>',len(nums))

# Time complexity is O(n^2) because of loop plus pop operation



##### Another Approach for O(n) #####

# Two pointer approach

def removeDuplicates(nums):
    i = 0

    for j in range(1, len(nums)):
        # If the current element is different from the last unique element
        if nums[j] != nums[i]:
            i += 1  # Move the pointer for unique elements
            nums[i] = nums[j]   #Place the new unique element at index i

    return i + 1
        
        

nums = [1, 2, 3, 4, 4, 5]
k = removeDuplicates(nums)
print(k)
print(nums[:k])