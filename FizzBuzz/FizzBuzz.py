for x in range(1,101):
    res = x
    if x % 3 == 0 and x % 5 == 0:
        res = "FizzBuzz"
    elif x % 3 == 0:
        res = "Fizz"
    elif x % 5 == 0:
        res = "Buzz"
    print(res)