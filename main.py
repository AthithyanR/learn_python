#!/usr/bin/python3
# from multiprocessing import Pool
# import os

# def sleepy(_):
#     os.system("aria2c")

# def start():
#     with Pool(5) as p:
#         p.map(sleepy, [None] * 5)

# if __name__ == "__main__":
#     start()

# list
# mylist = [2, 3, 4, 5, 1]
# print(2 in mylist)
# mylist.append(100)
# print(mylist)
# mylist.insert(0, -9)
# print(mylist)
# mylist.remove(4)
# print(mylist)

# print(len(mylist))
# print(mylist.index(100))
# print(sum(mylist))
# print(mylist.count(-5))

# mylist.reverse()
# print(mylist)
# mylist.sort()
# print(mylist)
# print(mylist[1:10:2])
# mylist.clear()
# print(mylist)

# mylist = [i*i for i in range(1, 6)]
# print(mylist)

# #tuples
# my_tuple = "athi", 24, "chennai"
# print(my_tuple, type(my_tuple))
# name, age, location = my_tuple
# print(name, age, location)
# name, *remaining = my_tuple
# #remaining is a list
# print(name, remaining)

# print("athi" in my_tuple)

# import sys
# print(sys.argv)
# print(sys.getsizeof("Athithyan"))

# my_dict = { "name": "athi", "age": 24 }
# my_dict["location"] = "chennai"
# new_dict = dict(my_dict) or my_dict.copy()
# dict(name="athi", age="24")
# del new_dict["locations"]
# new_dict.pop("location")
# print(my_dict, new_dict)
# print(my_dict.keys(), my_dict.values(), my_dict.items())

# print({"hello": 1} or [])

# my_set = set([1, 3, 4, 4])
# print(my_set)
''' other possible operations - union, intersection, difference, symmetric_difference,
update, intersection_update, difference update, symmetric_difference update, is_subset, is_superset, is_disjoint '''

# frozenset([1, 2, 3]) - immutable

# strings - do not += to a string (as usual)
# print("Hello there %s %s" % ("Athi", "r")) - old
# print("Hello there {} {}".format("Athi", "r")) - semi old
# f_name="Athi"
# l_name = "r"
# print(f"Hello there {f_name} {l_name}") - new

# collections - special data types