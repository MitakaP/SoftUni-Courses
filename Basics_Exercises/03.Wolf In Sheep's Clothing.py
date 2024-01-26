input_string = input()

animals = input_string.split(", ")

if animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    wolf_position = len(animals) - animals.index("wolf") - 1
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")
