n = int(input())
people = int(input())

if n % people == 0:
    result = int(n / people)
    print(result)
else:
    result = int(n / people) + 1
    print(result)
