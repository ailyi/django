import random

with open('List.txt') as f:
    lists = f.read().splitlines()


hangman = (
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
      +---+
      |   |
      o   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  | 
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      o   |
     /|\  |
     / \  |
          |
    =========
    """
)
guess_letters = []

fails = 0


def play_hangman(word_from_list):
    global fails
    fails = 0
    while True:
        print(hangman[fails])
        print('Guessed letters: ', ', '.join(guess_letters))
        guessed = ""
        for character in word_from_list:
            if character in guess_letters:
                guessed += character
            else:
                guessed += "-"
        print(guessed)
        input('Enter letter ')

        guess_letters.append()
        word_from_list.index()



while True:
    print('Enter 1 to play hangman, 2 to add a new word, 3 to quit program')
    user_action = int(input('Enter number: '))
    if user_action == 1:
        one_word_from_list = lists[random.randint(0, len(lists)-1)]
        play_hangman(one_word_from_list)
        break
    elif user_action == 2:
        word = input('Enter new word ')
        lists.append(word)
        print('Added', word)
    elif user_action == 3:
        print('Quit game!')
        break





