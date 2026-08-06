# Function without parameters: hardcoded greeting logic
def hello():
    print("Hello")


# Prompts user for input and calls hello(), printing name separately
name = input("What's your name? ")
hello()
print(name)