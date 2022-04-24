def primeOrNot():
    # Taking User's Input
    num = int(input("Enter any number: "))

    # Prime number is always greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

        '''
        If the entered number is less than or equal to 1
        That is not a prime number
        '''
    else:
        print(num, "is not a prime number")

primeOrNot()