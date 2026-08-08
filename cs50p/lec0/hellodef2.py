# Function with default parameter value ('world') if no argument is supplied
def hello(to="world"):
    print("hello,", to)


# Calling hello() with no arguments uses default value 'world'
hello()

# Prompts user for name and passes argument, overriding default
name = input("What's your name? ")
hello(name)