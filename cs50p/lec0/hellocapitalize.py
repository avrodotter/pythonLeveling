name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# It capitalizes only first letter of first word of the input
name = name.capitalize()

print(f"hello, {name}")