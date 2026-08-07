import subprocess

def greet_custom(name, speed=0, pitch=0, language="en-US"):
    greeting = f"Hello, {name}!"
    
    # -r = speed (-100 to 100)
    # -p = pitch (-100 to 100)
    # -l = language dialect (e.g., en-US, en-GB)
    command = [
        "spd-say", 
        "-r", str(speed), 
        "-p", str(pitch), 
        "-l", language, 
        greeting
    ]
    
    subprocess.run(command)
    return greeting

# Examples of different voice variations:
# 1. Default Voice
greet_custom("avro") 

# 2. Fast, High-Pitched Voice (Sounds energetic or cartoonish)
# greet_custom("avro", speed=30, pitch=40)

# 3. Slow, Deep-Pitched Voice (Sounds more robotic or serious)
# greet_custom("avro", speed=-20, pitch=-30)

# 4. British Accent variant (If en-GB is installed on your system)
# greet_custom("avro", language="en-GB")
