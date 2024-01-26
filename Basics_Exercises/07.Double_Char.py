while True:
    string = input()
    if string == "End":
        break
    elif string == "SoftUni":
        continue
    else:
        doubled_string = ''.join(char * 2 for char in string)
        print(doubled_string)
