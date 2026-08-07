import subprocess

def greet_with_side_effect():
    name = input("What's your name? ")
    greeting = f"Hello, {name}!"
    print(greeting)
    subprocess.run(["spd-say", greeting])
    return greeting

greet_with_side_effect()

# subprocess is a Python module that lets your Python program start and 
# communicate with other programs/processes running on your operating system.
# spd-say is not a Python function, it's a Linux command that makes your computer speak text aloud.
# so Python needs a way to tell the operating system: 
# "Run the spd-say program and give it this text."
# That's what subprocess.run() does.

"""
Your Python program
       ↓
subprocess.run()
       ↓
Operating System
       ↓
spd-say
       ↓
Computer speaks "Hello, Avro!"
"""