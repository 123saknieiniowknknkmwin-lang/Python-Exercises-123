
def exponential(number, exponent):
    return number ** exponent


numbers = [1, 2, 3, 4, 5]

x = list(map(lambda n: exponential(n, 10), numbers))
print(x)
