coffee_count = 0
while True:
    word = input()

    if word == "coding":
        coffee_count += 1
    elif word == "CODING":
        coffee_count += 2
    elif word == "movie":
        coffee_count += 1
    elif word == "MOVIE":
        coffee_count += 2
    elif word == "dog":
        coffee_count += 1
    elif word == "DOG":
        coffee_count += 2
    elif word == "cat":
        coffee_count += 1
    elif word == "CAT":
        coffee_count += 2
    elif word == "END":
        break


if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
