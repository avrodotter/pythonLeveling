# Function with a required parameter 'to' to dynamically greet the caller
def hello(to):
    print("hello, ", to)


# Prompts user for name and passes it as an argument into hello()
name = input("What's your name? ")
hello(name)

# In this example, `hello` is the name of the function, and it takes one parameter, `to`. 
# The code inside the function defines what happens when the function is called: 
# it returns a string that greets the person with their name.


# People often confuse arguments with parameters, but they represent two sides of the same coin.
# Parameter is The placeholder variable defined inside the function's parentheses. It acts like an empty box.
# An argument is the actual piece of data (like a text string, a number, or a list) that you pass into a function when you call it.