# Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
def to_underscore(string):
    new_string = ""
    try:
        for letter in string[1:]:
            if letter.isupper():
                new_string += "_"+letter.lower()
            else:
                new_string += letter
        title = string[0].lower()
        return title + new_string
    except:
        return str(string)
