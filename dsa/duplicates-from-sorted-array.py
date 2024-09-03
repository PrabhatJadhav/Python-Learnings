array =[1,1,2]
k=0

        
def duplicatesFromSortedArray():
    for indexOfTarget,number in enumerate(array):
        for indexOfNumberBeingSearched,num2 in enumerate(array):
            print('number',number,"and index ",indexOfTarget)
            print('2nd number',array[indexOfNumberBeingSearched+1],"amd index ",indexOfNumberBeingSearched+1)
           
            
            if number == array[indexOfNumberBeingSearched+1] and indexOfTarget == indexOfNumberBeingSearched+1:
                global k
                k+=1
                array.pop(indexOfNumberBeingSearched)
    
    
    
        
        
        
duplicatesFromSortedArray()
print("k ==>", k)
print("array ==>", array)

