# use open function and pass in the name of the file if they are in the same directory, else give relative / absolute path
#  Make sure you close the file as well
#  'readline' is like reading a line and moving the cursor below but 'readlines' function is better because it puts the lines in the list, readlines can be used in a loop as well

abc = open("abc.txt","r") 

print(abc.readable())

print(abc.read())

abc.close()