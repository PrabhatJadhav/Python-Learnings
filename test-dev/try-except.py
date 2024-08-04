def print_a_number(num):
    try:
        print(num)
    except ValueError:
        print("Invalid Input")
    except ZeroDivisionError as err:
        print("Zero Division Error ==> ",err)
        
user_number = input("Enter a number: ")

print_a_number(user_number)