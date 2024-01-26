beach_string = input()

lowercase_beach_string = beach_string.lower()

sand_count = lowercase_beach_string.count("sand")
water_count = lowercase_beach_string.count("water")
fish_count = lowercase_beach_string.count("fish")
sun_count = lowercase_beach_string.count("sun")

total_count = sand_count + water_count + fish_count + sun_count

print(total_count)
