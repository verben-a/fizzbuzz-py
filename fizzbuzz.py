n = input ("Please, enter the number: ")

for n in range(1,n):
    if n % 15 == 0:
        print ("fizzbuzz")
    elif n % 5 == 0:
        print ("buzz")
    elif n % 3 == 0:
        print ("fizz")
    else:
        print(n)