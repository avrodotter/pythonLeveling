import subprocess

def greet(name):
    greeting = f"Hello, {name}!"
    
    # This runs the spd-say command in your Ubuntu terminal
    # Securely triggers spd-say via subprocess
    subprocess.run(["spd-say", greeting])
    
    return greeting

greet("avro")

# You can quickly adjust the voice character archetype directly through the -t (or --voice-type) flag. 

# Female Voice: spd-say -t female1 "Hello avro"
# Child Voice: spd-say -t child_male "Hello avro"

# Available Built-in Archetypes:

# male1, male2, male3
# female1, female2, female3
# child_male, child_female