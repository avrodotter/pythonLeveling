import subprocess

def greet_scifi_droid(name):
    # Says "Hello friend" in Spanish
    greeting = f"Hola amigo {name}!"
    
    # -p 60 makes the voice squeaky and robotic
    command = ["spd-say", "-p", "60", "-l", "es-ES", greeting]
    
    subprocess.run(command)
    return greeting

greet_scifi_droid("avro")
