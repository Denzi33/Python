def sol():
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    ans = ""

    direction = input("Please input what do you want encryption or dencryption:\n")

    while direction.lower() not in ["encryption", 'e', "dencryption", 'd']:
     direction = input("Incorrect input! Please input again.\n")

    language = input("Please choose language Russian or English:\n")

    while language.lower() not in ['r', "rus", "russian", 'e', "eng", "english"]:
        language = input("Incorrect input! Please input again.\n")

    k = input("Please choose the step of encryption/decryption:\n")

    while not k.isdigit():
        k = input("Incorrect input! Please input again.\n")

    k = int(k)

    word = input("Input word for process:\n")

    if language.lower() in ['r', "rus", 'russian']:
        if direction.lower() in ['e', "encryption"]:
            for i in range(len(word)):
                if word[i] in upper_rus_alphabet:
                    ans += upper_rus_alphabet[(upper_rus_alphabet.index(word[i]) + k) % len(upper_rus_alphabet)]
                elif word[i] in lower_rus_alphabet:
                    ans += lower_rus_alphabet[(lower_rus_alphabet.index(word[i]) + k) % len(lower_rus_alphabet)]
                else:
                    ans += word[i]
        elif direction.lower() in ['d', "decryption"]:
            for i in range(len(word)):
                if word[i] in upper_rus_alphabet:
                    ans += upper_rus_alphabet[(upper_rus_alphabet.index(word[i]) - k) % len(upper_rus_alphabet)]
                elif word[i] in lower_rus_alphabet:
                    ans += lower_rus_alphabet[(lower_rus_alphabet.index(word[i]) - k) % len(lower_rus_alphabet)]
                else:
                    ans += word[i]
    elif language.lower() in ['e', "eng", 'english']:
        if direction.lower() in ['e', "encryption"]:
            for i in range(len(word)):
                if word[i] in upper_eng_alphabet:
                    ans += upper_eng_alphabet[(upper_eng_alphabet.index(word[i]) + k) % len(upper_eng_alphabet)]
                elif word[i] in lower_eng_alphabet:
                    ans += lower_eng_alphabet[(lower_eng_alphabet.index(word[i]) + k) % len(lower_eng_alphabet)]
                else:
                    ans += word[i]
        elif direction.lower() in ['d', "decryption"]:
            for i in range(len(word)):
                if word[i] in upper_eng_alphabet:
                    ans += upper_eng_alphabet[(upper_eng_alphabet.index(word[i]) - k) % len(upper_eng_alphabet)]
                elif word[i] in lower_eng_alphabet:
                    ans += lower_eng_alphabet[(lower_eng_alphabet.index(word[i]) - k) % len(lower_eng_alphabet)]
                else:
                    ans += word[i]

    print(ans)

sol()
