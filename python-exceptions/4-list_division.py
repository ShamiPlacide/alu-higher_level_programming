#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            # Check if both elements are integers or floats.
            if type(a) not in (int, float) or type(b) not in (int, float):
                raise TypeError
            if b == 0:
                raise ZeroDivisionError
            division = a / b
        except IndexError:
            print("out of range")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0
        finally:
            new_list.append(division)
    return new_list

