# Vowels change to 5 in our language

vowels = ['a','e','i','o','u']

def translator_func(phrase):
    translation=""
    for alphabet in phrase:
        if alphabet.lower() in vowels:
            if alphabet.isupper():
                translation += '0'
            else:
                translation += '5'
            
        else:
            translation += alphabet
            
    return translation

user_input = input("Enter a phrase or a word: ")
        
print(translator_func(user_input))