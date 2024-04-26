f = lambda x, y: x + y
print("when used lambda, the result of 'f' is ", f(2, 1))

nums = [1, 2, 3, 4, 5]
result = map(lambda x: x + 1, nums)
print("after mapping the  result is ",list(result))
