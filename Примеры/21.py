def get_sum(a, b, c):
    total += a + b + c
    print(total)


total = 0
get_sum(1, 2,
        3)  # UnboundLocalError: local variable 'total' referenced before assignment
print(total)
