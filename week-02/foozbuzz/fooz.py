
#input is used to read integers 
countNumber = input("What number do you want to count to?")
#fob(countNumber)

#def fob(countNumber) 
for x in range(countNumber) :
    print (x) 
    if x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
