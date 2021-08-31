def reversed_args(f):
    def g(*args):
        return f(*reversed(args))
    return g

# reversed_args = lambda f: lambda *a: f(*reversed(a))


def pow2(a, b):
    return pow(a, b)


print(reversed_args(pow2)(2, 3))
print(pow2(2, 3))
