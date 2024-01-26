
budget = float(input())
flour_price_per_kg = float(input())

egg_price_per_pack = 0.75 * flour_price_per_kg
milk_price_per_liter = 1.25 * flour_price_per_kg

eggs = 0
money_spent = 0
colored_eggs = 0
loaves = 0

while budget >= flour_price_per_kg + egg_price_per_pack + 0.25 * milk_price_per_liter:
    budget -= flour_price_per_kg + egg_price_per_pack + 0.25 * milk_price_per_liter
    money_spent += flour_price_per_kg + egg_price_per_pack + 0.25 * milk_price_per_liter
    eggs += 3
    colored_eggs += 3
    loaves += 1

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
