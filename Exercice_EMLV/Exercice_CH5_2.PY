'''Write a script asking the user his age. If the user is :
Less than 18 : he is a child
 from 18 to 50 (18 including, 50 excluding) : he is a young adult
old from 50 to 70 (50 including) : he is an old man
very old more than 70 (70 including) : he is a very old man'''


age = int(input("What's your age ?"))

if age < 18:
    print("he is a child")
elif age >= 18 and age < 50:
    print("he is a young adult")
elif age >= 50 and age < 70:
    print("he is an old man")
elif age >= 70 :
    print("he is a very old man")




'''
# Return True when the parameter is more than 6 characters long and False when it's not
def long_text(text):
    return len(text) > 6

print(long_text("Hellooeorjore?.!"))


# return True when his parameter has "?", "." or "!" inside and False in other cases.
def special_character(space) :
    return all(symbol in space for symbol in ("?", ".", "!"))

print(special_character("Hellooeorjore?.!"))


#1ère manière de faire
def good_password(password):
    return long_text(password) and special_character(password)

#2ème manière de faire
def good_password(password):
    return all(func(password) for func in (long_text, special_character))'''