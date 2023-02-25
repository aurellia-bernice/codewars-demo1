# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

# For instance:

# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord
def camel_case(string):
    strin_ = string.split(" ")
    new_value = ""
    for i in strin_:
        s_ = i[:1].upper()
        s__ = i[1:]
        new_value += s_ + s__
    return new_value
