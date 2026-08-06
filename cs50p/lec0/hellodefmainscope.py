def main():
    name = input("What's your name? ")
    hello()
    # The variable `name` is local to main(), so it is not available in hello()
        # unless we pass it as an argument. So this will throw a name-error

def hello():
    print("Hello,", name)
    
main()

"""
Scope is the visibility or lifetime of a variable within the program.
In this context, scope means the part of the program where a variable can be used.

Why it matters:

A variable defined inside a function is usually only available inside that function.
If another function tries to use it, Python will not see it there 
unless it is passed in or declared in a broader scope.
This is why the code in your example failed: 
the name variable existed inside main(), but hello() could not access it directly.

"""