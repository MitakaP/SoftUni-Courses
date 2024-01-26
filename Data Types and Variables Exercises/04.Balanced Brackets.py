n = int(input())
openingBracket, closingBracket = "(", ")"
brackets = []
for i in range(n):
    exp = input()
    if exp == openingBracket:
        brackets.append(exp)
    elif exp == closingBracket:
        brackets.append(exp)
for i in range(len(brackets)):
    if i % 2 == 0:
        if brackets[i] != openingBracket:
            print("UNBALANCED")
            break
    else:
        if brackets[i] != closingBracket:
            print("UNBALANCED")
            break
else:
    print("BALANCED")
