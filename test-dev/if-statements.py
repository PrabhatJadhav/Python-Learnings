is_male=True
is_tall=False

if is_male and is_tall:
    print("Is a Male and Tall")
elif is_male and not(is_tall):
    print("Is a Male but not Tall")
elif is_tall and not(is_male):
    print("Is Tall but not a Male")
else:
    print("No Match Found")
    