def flipbits(num1, num2):
    flip = 0
    while(num1 > 0 or num2 > 0):
        t1 = num1 & 1
        t2 = num2 & 1
        if t1 != t2:
            flip += 1
        num1 >>=1
        num2 >>=1
    return flip
num1 = int(input("enter fisrt number:"))
num2 = int(input("enter second number:"))
print("number of flips needed: ",flipbits(num1, num2))