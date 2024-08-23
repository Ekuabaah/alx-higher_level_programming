#!/usr/bin/python3
def no_c(my_string):
    characters_to_remove = 'cC'
    new_string = ''
    for m in my_string:
        if m not in characters_to_remove:
            new_string += m
    return (new_string)
