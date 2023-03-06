# description
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# my code
def to_camel_case(text):
    import string
    text_ = ""
    new_text = ""
    new_text_ = ""
    new_string = []
    alphabet = list(string.ascii_lowercase)
    for i in text:
        if i.lower() in alphabet:
            text_ += i
        else:
            text_ += " "
    new_string = text_.split(" ")
    for i in new_string[1:]:
        new_ = new_string[0]
        new_text_ = new_
        if i != new_string[0]:
            new_text += i.title()
    return new_text_ + new_text
