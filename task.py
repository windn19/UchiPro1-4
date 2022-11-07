lst = [1] * 10
print(lst)

lst = lst + ['string']
print(lst)
lst[4] = 189
print(lst)
lst.append(['a', 'b', 'c', 'hello'])
print(lst)
lst[-3] = (1, 6, 89)
print(lst)
print(lst[0])
lst.remove(189)
lst.pop()
print(lst)
print(lst.count(1))
# print(sorted(lst))
lst = list(range(10, 0, -1))
print(lst)
lst.sort()
print(lst)

