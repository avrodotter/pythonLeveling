# taking input from user
# Put a zero in for the unknown value

print("n1/d1 = n2/d2\n Enter the known numbers and put zero for the unknown value\n")
print("this is a program to find djjihu hd")

n1 = int(input("n1 = "))
d1 = int(input("d1 = "))
n2 = int(input("n2 = "))
d2 = int(input("d2 = "))

if n1 == 0:
    answer = n2 * d1 / d2
    print("n1 =", answer)

if d1 == 0:
    answer = n1 * d2 / n2
    print("d1 =", answer)

if n2 == 0:
    answer = d2 * n1 / d1
    print("n2 =", answer)

if d2 == 0:
    answer = n2 * d1 / n1
    print("d2 =", answer)