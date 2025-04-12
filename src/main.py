def my_func(my_list, my_type):
    count = 0
    for item in my_list:
        if type(item) == my_type:
            count += 1
    return count

#
# if __name__ == "__main__":
#
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], int) == 3
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], str) == 1
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], float) == 1
#     assert my_func([1, "Маша", 3.9, [], {}, 4, 5], list) == 1
#
