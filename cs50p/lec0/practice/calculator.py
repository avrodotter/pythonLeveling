x = float(input("x = "))
y = float(input("y = "))

addition = x+y
substraction = x-y
multiplication = x*y
division = x/y
remainder = x%y

print(f"Sum of x & y is {addition}")
print(f"Substruction of x & y is {substraction}")
print(f"Multiplication of x & y is {multiplication}")
print(f"Division of x & y is {division}")
print(f"Remainder of x/y is {remainder}")

print(f"Rounded of divion = {round(division)}")
print(f"Rounded of division upto 2 decimals = {round(division,2)}")
print(f"Rounded of division upto 3 decimals = {division:.3f}")
