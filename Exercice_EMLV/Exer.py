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
    return all(func(password) for func in (long_text, special_character))







print(good_password("Hellooeorjore?.!"))