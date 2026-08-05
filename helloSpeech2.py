import subprocess

def greet(name):
    greeting = f"Hello, {name}!"
    
    # Customizes the voice signature directly through python
    subprocess.run(["spd-say", "-t", "female1", greeting])
    
    return greeting

greet("avro")
