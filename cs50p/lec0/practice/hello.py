name = input("What's your name? ").strip().title()
first, last = name.split()
print("Hello,", first)

age = input(f"What's your age {first}? ")
print(f"So you are {age} years old.")

location = input("Which city do you live in? ").strip().capitalize()
print(f"So you live in {location}.")

desired_name = input("What do you want to be called? ").strip()
print(f"So I should call you \"{desired_name}\".")

earning = int(input("How much rupees do you earn in a month? "))
print(f"{earning:,}", end=" Rupees")

greeting = f"\nSo Mr. {name}, you are {age} years old, you live in {location} and you earn Rs {earning} per month. I will call you {desired_name} from now."
print(greeting)