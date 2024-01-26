# n = int(input())
#
# for _ in range(n):
#     word = input()
def check_purity(string):
    forbidden_characters = {',', '.', '_'}
    if all(char not in forbidden_characters for char in string):
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')


def main():
    n = int(input())

    for _ in range(n):
        current_string = input()
        check_purity(current_string)


if __name__ == "__main__":
    main()
