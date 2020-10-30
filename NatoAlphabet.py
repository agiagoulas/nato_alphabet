import random


def learn_nato_alphabet():
    nato_alphabet = {
        "A": "Alfa",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-Ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }

    print("Welcome to the Nato Alphabet learning program!")
    print("You have to type in the matching words to the letters.")
    print("Type in 'exit' to exit at any time")
    mode = input("Select mode by typing 'order'/'random': ")
    if mode == "exit":
        print("See you next time!")
        return ()

    learned_counter = 0
    true_counter = 0
    wrong_counter = 0

    if mode == "order":
        for pair in nato_alphabet:
            print("")
            print(pair)
            typed_answer = input("Input: ")
            if typed_answer == "exit":
                print("")
                print("See you next time!")
                print(f"You got {true_counter} out of {learned_counter} answered pairs right!")
                return ()
            elif typed_answer == nato_alphabet[pair]:
                learned_counter += 1
                true_counter += 1
                print("That´s right!")
            else:
                learned_counter += 1
                wrong_counter += 1
                print(f"That´s wrong, the wright answer is '{nato_alphabet[pair]}'")
        print("")
        print("See you next time!")
        print(f"You got {true_counter} out of {learned_counter} answered pairs right!")
    elif mode == "random":
        while True:
            random_index = random.randrange(0, (len(nato_alphabet) - 1), 1)
            keys = list(nato_alphabet.keys())
            pair = keys[random_index]
            print("")
            print(pair)
            typed_answer = input("Input: ")
            if typed_answer == "exit":
                print("")
                print("See you next time!")
                print(f"You got {true_counter} out of {learned_counter} answered pairs right!")
                return ()
            elif typed_answer == nato_alphabet[pair]:
                learned_counter += 1
                true_counter += 1
                print("That´s right!")
            else:
                learned_counter += 1
                wrong_counter += 1
                print(f"That´s wrong, the wright answer is '{nato_alphabet[pair]}'")


learn_nato_alphabet()
