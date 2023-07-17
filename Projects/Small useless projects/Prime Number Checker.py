import sys


def check_if_primenum(num):
    for number in range(2,num):
        if num % number ==0:
            print("It is not a prime number")
            sys.exit()
    print("It is a prime number")

num = int(input("Enter a number: > "))
check_if_primenum(num)