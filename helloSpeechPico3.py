import subprocess

def greet_french_style(name):
    # Says "Welcome" in French
    greeting = f"Bienvenue, {name}."
    
    # Keeps default pitch but enforces French phonetic rules
    command = ["spd-say", "-p", "0", "-l", "fr-FR", greeting]
    
    subprocess.run(command)
    return greeting

greet_french_style("avro")
