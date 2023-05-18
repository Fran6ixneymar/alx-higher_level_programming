#!/usr/bin/python3
def search_replace(my_list, search, replace):
    start_list = list(map(lambda x: replace if x == search else x, my_list))
    return (start_list)

