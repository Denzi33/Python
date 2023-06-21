from random import choice

def get_word(words):
    return choice(words).lower()

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    play_key = True

    print("Hello, let's start to play hangover.")

    while play_key:
        word_completion = '_' * len(word)
        guessed = False
        guessed_letters = []
        guessed_words = []
        tries = 6

        easy = input("Do you wanna play on easy level?\n")

        while easy.lower() not in ["yes", 'y', 'n', "no"]:
            easy = input("Incorrect input! Try again:\n")

        if easy.lower() in ["yes", 'y']:
            word_completion = word[0] + word_completion[1:-1] + word[-1]

        while tries >=1 and (not guessed):
            print(display_hangman(tries))
            print(word_completion)

            char = input("Please, input a character or a word:\n")

            while True:
                key = True

                if not (len(char) == len(word) or len(char) == 1):
                    char = input("Incorrect input! Please, try again:\n")
                    continue

                if len(char) == len(word):
                    if char.lower() in guessed_words:
                        char = input("Incorrect input! Please, try again:\n")
                        continue

                    for i in char:
                        if i.lower() not in "abcdefghijklmnopqrstuvwxyz":
                            char = input("Incorrect input a word! Please, try again:\n")
                            key = False
                            break

                    if not key:
                        continue
                if len(char) == 1:
                    if char.lower() not in "abcdefghijklmnopqrstuvwxyz" or (char.lower() in guessed_letters):
                        char = input("Incorrect input a letter! Please, try again:\n")
                        continue
                break

            if len(char) == len(word):
                if char.lower() != word:
                    tries -= 1
                    guessed_words.append(char.lower())
                else:
                    word_completion = word

            if len(char) == 1:
                if char.lower() not in word:
                    tries -= 1
                    guessed_letters.append(char.lower())
                else:
                    for i in range(len(word_completion)):
                        if word[i] == char.lower():
                            word_completion = word_completion[:i] + char.lower() + word_completion[i + 1:]

            if word.lower() == word_completion.lower():
                guessed = True
                break

        if tries == 0:
            print(f"You lose! The hidden word is {word}!")
        else:
            print(f"Congratulations you won! The hidden word is {word}!")

        ans = input("Do you want to play again?\n")

        while ans.lower() not in ["yes", "no", 'n', 'y']:
            ans = input("Incorrect input! Please, try again:\n")

        if ans.lower() == 'n' or ans.lower() == 'no':
            play_key = False

            print("Good bye!")
        else:
            word = choice(word_list)

word_list = ["dog", "cat", "man", "girl", "monkey", "horse", "power", "hat", "pen"]

play(get_word(word_list))
