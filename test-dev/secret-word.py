secret_word="apple"
user_input=""
guess_count=0
guess_limit=3
is_guess_correct=False

while not(is_guess_correct) :
    if not(is_guess_correct) and guess_count < guess_limit:
        user_input=input("Guess the word: ")
        guess_count +=1
        is_guess_correct=False
    else:
        is_guess_correct=True
        break

if (guess_count < guess_limit) and is_guess_correct:
    print("Correct Guess ==> " + user_input)
    print("Guessed In ==> " , guess_count , " tries")
else:
    print("Guess Limit reached, you had",guess_limit,"guesses, YOU LOSE!!!")
            
    
