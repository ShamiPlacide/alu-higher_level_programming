#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            # Attempt to access the element at index i.
            element = my_list[i]
        except Exception:
            # If the element cannot be accessed, break out of the loop.
            break
        try:
            # Try to print the element as an integer.
            print("{:d}".format(element), end=" ")
            printed += 1
        except Exception:
            # If formatting fails, skip this element.
            continue
    print("")
    return printed

