"""
    ARE YOU HUNGRY MY CHILD ??
"""

hungry = input("Are you hungry?: ")

food = []
with open('food_items.txt', 'r') as f:
    for food_item in f:
        food.append(food_item.strip())

if hungry == "yes":
    query = input("Okayy..so what would you like to have?")
    if query in food:
        print("Great, please hang on!")
    else:
        print("Okay, since you don't know, let me list the things for you.")
        print(f"{(', ').join(food)}")
else:
    print("do your homework")