number = int(input("Enter a number: "))

def Disarium(num):
    
    num_str = str(num)
    lenght = len(num_str)

    digit = 1
    num1 = int(num_str[0])
    num2 = 0
    
    while digit < lenght:    
        num2 = int(num_str[digit])
        i = 0

        while i < digit:
            num2 = num2 * int(num_str[digit])
            i += 1
        
        num1 = num1 + num2
        digit += 1
             
    if num1 == num:
        return (num, "is Disarium")
    else: 
        return (num, "isn't Disarium")

print(Disarium(number))