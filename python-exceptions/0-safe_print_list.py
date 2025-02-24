#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Attempt to access the element at index i.
            element = my_list[i]
            # Print the element followed by a space (without a newline).
            print(element, end=" ")
            count += 1
        except Exception:
            # If accessing my_list[i] fails (likely IndexError), stop printing.
            break
    # Print a newline after printing all elements.
    print("")
    return count

