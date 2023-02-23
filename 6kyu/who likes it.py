# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

def likes(names):
    add = " and "
    newstring = ""
    calculated_valu = len(names)-2
    calculated_value = str(calculated_valu)
    another_text = " like this"

    if len(names) == 0:
        newstring = "no one likes this"
        return newstring
    if len(names) == 1:
        for i in names:
            newstring = i + " likes this"
            return newstring
    elif len(names) == 2:
        for i in range(1, len(names)):
            newstring = names[i-1]+add + names[i-2]+another_text
            return newstring
    elif len(names) == 3:
        for i in range(1, len(names)-1):
            newstring = names[i-1]+", " + \
                names[i-3]+add+names[i-2]+another_text
            return newstring
    elif len(names) > 3:
        for i in range(1, 2):
            for i in range(1, 2):
                newstring = names[i-1]+", " + names[i-len(names)]
        newstring = newstring + add + calculated_value + " "+"others"+""+another_text
        return newstring
