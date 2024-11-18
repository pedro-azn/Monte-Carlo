def long_text(x):
    return len(x) > 6

print(long_text("Hellodedded"))



def special_character(space) :
    return all(symbol in space for symbol in ("?", ".", "!"))

def special_character(space):
    return set("?.!") <= set(space)

def special_character(space):
    return all(map(lambda symbol: symbol in space, ("?", ".", "!")))




Create a function good_password(text) giving True when both of previous conditions are respected.


