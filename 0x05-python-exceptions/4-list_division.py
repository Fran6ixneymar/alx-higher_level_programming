#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    start_list = []
    for fig in range(list_length):
        try:
            result = my_list_1[fig] / my_list_2[fig]
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            start_list.append(result)
    return start_list
