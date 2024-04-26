"""
single argument
"""
q = lambda a: a + 10
print(q(5))

"""
multiple argument
"""
w = lambda a, b, c, d: a + b + c * d + a
print(w(2, 8, 9, 6))

"""
lambda on a function
"""


def sample(x):
    return lambda a: a + x


anw = sample(2)
print(anw(5))
