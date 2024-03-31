#!/usr/bin/python3

my_list = []
my_list.extend([10, 20, 30, 40])
my_list.insert(1, 15)
my_list.extend([50, 60, 70])
my_list.pop()
my_list.sort()
element = 30
index_element = my_list.index(element)
print(index_element)
