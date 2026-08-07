import subprocess

def greet_british_butler(name):
    # Formats a formal greeting statement
    greeting = f"Good day, master {name}. Welcome back."
    
    # -p -40 lowers the pitch drastically for a deep voice
    command = ["spd-say", "-p", "-40", "-l", "en-GB", greeting]
    
    subprocess.run(command)
    return greeting

greet_british_butler("avro")
