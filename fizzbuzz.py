def fizzBuzz(n):
    r = [item+1 for item in range(n)]
    for i in r:
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

fizzBuzz(10)
