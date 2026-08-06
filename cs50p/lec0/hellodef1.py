# Function with a required parameter 'to' to dynamically greet the caller
def hello(to):
    print("hello, ", to)


# Prompts user for name and passes it as an argument into hello()
name = input("What's your name? ")
hello(name)