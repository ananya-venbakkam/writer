num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

if(num1 > num2 and num1 > num3):
    g1 = num1

    if(num2 > num3):
        g2 = num2
        g3 = num3
    else:
        g2 = num3
        g3 = num2

else if(num2 > num1 and num2 > num3):
    g1 = num2

    if(num1 > num3):
        g2 = num1
        g3 = num3
    else:
        g2 = num3
        g3 = num1
else if(num3 > num1 and num3 > num2):
    g1 = num3

    if(num1 > num2):
        g2 = num1
        g3 = num2
    else:
        g2 = num2
        g3 = num1

s1 = g1^2
s2 = g2^2
s3 = g3^3

if(s1 is (s2+s3)):
    print("The numbers fom a Pythagorean triplet")
else:
    print("They do not foram a Pythagorean triplet")
