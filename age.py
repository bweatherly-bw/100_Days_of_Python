# This application will determine the age of the user 

name = input('What is your name? ')
birth_year = input('What year were your born? ')
current_year = 2024

# 
# Could add an age calc that will tell the user exactly how old they are
# Years, months, and days 
# 

your_age = current_year - int(birth_year)

print(f'Hello, {name} you are currently {your_age} years old.')
print("Testing from a new machine")