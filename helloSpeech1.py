import subprocess

def greet(name):
    greeting = f"Hello, {name}!"
    
    # Securely triggers spd-say via subprocess
    subprocess.run(["spd-say", greeting])
    
    return greeting

greet("avro")
