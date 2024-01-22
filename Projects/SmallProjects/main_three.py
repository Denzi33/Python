from random import choice

def generate_password(length, chars):
    answer = ""

    for i in range(length):
        answer += choice(chars)

    return answer

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
ambiguous = "il1Lo0O"

n = input("Input number of passwords:\n")

while not n.isdigit() or int(n) < 1:
    n = input("Incorrect input! Please, input again.\n")

for j in range(int(n)):
    chars = ''

    l = input("Input length of password:\n")

    while not l.isdigit() or int(l) < 8:
        l = input("Incorrect input! Please, input again.\n")

    key1 = input("Do you want to use digits in password?\n")

    while key1.lower() not in ["yes", 'y', 'n', "no"]:
        key1 = input("Incorrect input! Please input again.\n")

    if key1.lower() in ["yes", 'y']:
        chars += digits

    key2 = input("Do you want to use lowercase letters in password?\n")

    while key2.lower() not in ["yes", 'y', 'n', "no"]:
        key2 = input("Incorrect input! Please input again.\n")

    if key2.lower() in ["yes", 'y']:
        chars += lowercase_letters

    key3 = input("Do you want to use uppercase letters in password?\n")

    while key3.lower() not in ["yes", 'y', 'n', "no"]:
        key3 = input("Incorrect input! Please input again.\n")

    if key3.lower() in ["yes", 'y']:
        chars += uppercase_letters

    key4 = input("Do you want to use symbols of punctuation in password?\n")

    while key4.lower() not in ["yes", 'y', 'n', "no"]:
        key4 = input("Incorrect input! Please input again.\n")

    if key4.lower() in ["yes", 'y']:
        chars += punctuation

    key5 = input("Do you want to delete ambiguous symbols in password?\n")

    while key5.lower() not in ["yes", 'y', 'n', "no"]:
        key5 = input("Incorrect input! Please input again.\n")

    if key5.lower() in ["yes", 'y']:
        for i in chars:
            if i in ambiguous:
                chars = chars.replace(i, '')

    print(f"Your passwrod № {j} with length = {n} is {generate_password(int(l), chars)}")

print("That is all. See you later.")
