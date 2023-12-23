#wap program to check input number is prime or not
'''
n = int(input('Enter any number:'))
if n<=1:
    print("It is a not Prime Number")
else:
    is_prime = True
    for i in range(2,n//2+1):
        if n%i==0:
            is_prime= False
            break
    if is_prime==True:
        print("It is a Prime Number")
    else:
        print("It is a not Prime Number")
'''
#wap to generate prime numbers which are less than or equal the given numbers
'''
n = int(input('Enter the number:'))
n1 = 2
while n1 <= n:
    is_prime = True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime= False
            break
    if is_prime==True:
        print(n1)
    n1 = n1+1
'''
#wap to generate first n prime numbers

n = int(input('Enter the number:'))
count = 0
n1 = 2
while True:
    is_prime = True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime= False
            break
    if is_prime==True:
        print(n1)
        count = count+1
    if count==n:
        break
    n1=n1+1
