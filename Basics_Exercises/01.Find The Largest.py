number = input()

digits = [int(digit) for digit in str(number)]

sorted_digits = sorted(digits, reverse=True)

largest_number = int(''.join(map(str, sorted_digits)))

print(largest_number)
