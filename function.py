def area(a, b=4):
    return a*b


print(area(4, 5))
print(area(b=4, a=3))
print(area(4))
# print(area(b=5)) it does not work
print(area(a=1))


def mean(*args):
    return sum(args) / len(args)


print(mean(2, 3, 4, 5, 6))


def foo(**kwargs):
    return kwargs


print(foo(a=1, b=3, c=4))
