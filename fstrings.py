def manual_str_formatting(name, subscribers):
    if subscribers > 100000:
        print("Wow " + name + " You have " + subscribers + " subcribers! This is awesome!")
    else:
        print("Only " + subscribers + "?")

def fstrings(name, subscribers):
    if subscribers > 100000:
        print(f"Wow {name} You have {subscribers} subcribers! This is awesome!")
    else:
        print(f"Only {subscribers}?")