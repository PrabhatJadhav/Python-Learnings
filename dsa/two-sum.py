array =[2,7,11,6]
target=13

        
def twoSum(nums, target):
    numbers_dictionary = dict()
    
    for index,a_number in enumerate(nums):
        target_number = abs( target - a_number)
        
        
        if target_number in numbers_dictionary:
            return [index,numbers_dictionary[target_number]]
        
        numbers_dictionary[a_number]=index
        
        
        
print("Answer ==>",twoSum(array,target))

