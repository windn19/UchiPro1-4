def to_list(lst):
    if type(lst) != list:
        return [lst]
    else:
        if lst:
            return to_list(lst[0]) + to_list(lst[1:])
        else:
            return []


print(to_list([1, 2, 3, 4, [5]]))
print(to_list([1, 2, 3, [4, [5]]]))
print(to_list([[1], [[[2]]], [3, [4, [5]]]]))
print(to_list([1, [[2], [3, [4]]], [[[[[5]]]]]]))
