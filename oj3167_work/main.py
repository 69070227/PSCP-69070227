"""FizzBuzz"""

num = int(input())

for i in range(1,num+1):
    if not i % 3 and  i % 5:
        i = "Fizz"
        print(i)
    elif not i % 5 and  i % 3:
        i = "Buzz"
        print(i)
    elif not i % 3 and not i % 5:
        i = "FizzBuzz"
        print(i)
    else:
        print(i)
