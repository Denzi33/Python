from random import choice

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print("Hello, world! I'm magic ball and I know all answers on any your question.")

name = input("What is your name?\n")

print(f"Hello {name}! Let is start game.")

while True:
    question = input("Write down what do you want to know:\n")

    print("Answer is:", choice(answers))

    answer = input("Do you want to ask something again?")

    while answer.lower() not in ['y', 'n', "yes", "no"]:
        answer = input("Incorrect input! Please, answer again.\n")

    if answer.lower() in ['n', "no"]:
        print("Ok. See you later.")
        break