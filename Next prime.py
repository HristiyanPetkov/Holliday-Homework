number = int(input("Enter a number: "))

def next_prime(num):
    num = num + 1
    loop = 0
    while True:
        for i in range(2, num):
            if (num % i) == 0:
                loop = loop + 1
                break
        if loop == 0:
            return num
        loop = 0
        num = num + 1

print("Next prime number: ", next_prime(number))
