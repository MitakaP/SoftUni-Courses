key = int(input())
n = int(input())

my_list = []

for i in range(n):
    char = input()
    char_number = ord(char)
    shifted = char_number + key
    again_shifted = chr(shifted)
    my_list.append(again_shifted)

print("".join(my_list))
