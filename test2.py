def is_prime(num):
    if num <= 1:
        print(f"{num} is not a prime number")
        return

    c = 0
    for i in range(1, num+1):
        if num % i == 0:
            c += 1

    if c > 2:
        print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

is_prime(int(input("enter num \n")))
