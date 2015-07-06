import random  # import for random picking of word


def get_words_from_file():
    """This function reads in words from a file and puts them
    in a list."""
    count = 0
    list_of_words = []
    with open("/usr/share/dict/words") as file_words:
        word = file_words.readline()
        while word != '':
            list_of_words.append(word.strip())
            count += 1
            word = file_words.readline()
    return list_of_words


def ask_for_difficulty():
    """This function asks the user what difficulty they
    want to play in the game."""
    user_input_mode = ""
    print("Hello, welcome to the Mystery Word game! ")
    while True:
        user_input_mode = \
            input("What level of difficulty? Type in 'easy', "
                  "'normal', or 'hard': ")
        if (user_input_mode.lower() == "easy") or \
                (user_input_mode.lower() == "normal") or \
                (user_input_mode.lower() == "hard"):
            break
        else:
            print("Sorry, you made an invalid input!  Print enter again. ")
            continue
    return user_input_mode.lower()


def grab_a_word(the_list, difficulty):
    """grabs a list of words from the whole list based on the
    difficulty, calls correct function for that"""
    if difficulty == "easy":
        the_list_chosen = easy_words(the_list)
    elif difficulty == "normal":
        the_list_chosen = medium_words(the_list)
    elif difficulty == "hard":
        the_list_chosen = hard_words(the_list)
    else:
        the_list_chosen = ""
    return the_list_chosen


def easy_words(easy_list):
    """Chooses the words that belong in the easy list from the whole
    list and returns the easy list."""
    temp_easy_list = []
    for word in easy_list:
        if (len(word) >= 4) and (len(word) <= 6):
            temp_easy_list.append(word)
        else:
            continue
    return temp_easy_list


def medium_words(medium_list):
    """Chooses the words that belong in the normal/medium list
    from the whole list and returns the normal/medium list.
    """
    temp_medium_list = []
    for word in medium_list:
        if (len(word) >= 6) and (len(word) <= 8):
            temp_medium_list.append(word)
        else:
            continue
    return temp_medium_list


def hard_words(hard_list):
    """Chooses the words that belong in the hard list from the whole
    list and returns the hard list."""
    temp_hard_list = []
    for word in hard_list:
        if len(word) >= 8:
            temp_hard_list.append(word)
        else:
            continue
    return temp_hard_list


def random_word(the_word_list):
    """Returns a word from the list passed in based on a random index."""
    list_size = len(the_word_list)
    random_index = random.randint(0, list_size - 1)
    return the_word_list[random_index]


def get_user_letter_input():
    """Gets user letter guess and decides if it is valid"""
    valid_guess = False
    letter_guess = ""
    while not valid_guess:
        letter_guess = input("Please enter your guess for a "
                             "letter in the word: ")
        if len(letter_guess) > 1:
            print("Invalid entry, you entered too many letters.")
            valid_guess = False
        elif (len(letter_guess) == 1) and (letter_guess.isalpha()):
            valid_guess = True
        elif (len(letter_guess) == 1) and \
                (not letter_guess.isalpha()):
            print("Invalid entry, you did not enter an "
                  "alphabetical character.")
            valid_guess = False
        else:
            print("Invalid entry, not a valid letter.")
            valid_guess = False
    return letter_guess.lower()


def letter_in_word(chosen_word, user_letter, found_so_far):
    """Returns a list representation of the word where guessed letters
     are filled in and _ where not guessed """
    index = 0
    while index <= len(chosen_word) - 1:
        if user_letter == chosen_word[index]:
            found_so_far[index] = user_letter
            index += 1
        else:
            index += 1
    if user_letter in chosen_word:
        print("Congratulations, your letter guess appears in the "
              "mystery word.")
    else:
        print("Sorry, that letter guess does not appear in the "
              "mystery word.")
    return found_so_far


def set_default_word(picked):
    """Sets a default list to characters of all _ as letters not
    correctly chosen yet"""
    quick_index = 0
    found = []
    while quick_index <= len(picked) - 1:
        found.append('_')
        quick_index += 1
    return found


def display_word(word, list_of_letters):
    """Displays the word with known characters and unknown _"""
    size_of = 0
    count = 0
    new_string = ""
    size_of = len(list_of_letters)
    while count <= (size_of - 1):
        new_string += list_of_letters[count]
        new_string += ' '
        count += 1
    print(new_string)


def is_word_complete(word, person_list):
    """Compares the computer chosen word with the list of letters
    chosen by player and returns True if equal"""
    temp_word = ""
    temp_word = temp_word.join(person_list)
    if word == temp_word:
        return True
    else:
        return False


if __name__ == '__main__':
    # do whatever when the file is run directly

    letter = ""  # letter chosen by player
    guess_count = 1  # round game is on
    found_already = []  # the word in list format
    player_found_word = ""

    word_list = get_words_from_file()  # read in words from a file
    input_from_user = ask_for_difficulty()  # get user to choose
    list_picked = grab_a_word(word_list, input_from_user)  # grab list of words
    word_picked = random_word(list_picked).lower()  # pick the actual word
    print("The word you will try and guess has {} letters in it.".
          format(len(word_picked)))
    found_already = set_default_word(word_picked)
    player_found_word = player_found_word.join(found_already)
    print()
    while guess_count < 9:
        count_boolean = False
        print("This is round {} for the game."
              .format(guess_count))
        while True:
            letter = get_user_letter_input()
            if letter in player_found_word:
                print("You already chose that letter, please enter a "
                      "different letter.")
            else:
                found_already = letter_in_word(word_picked, letter,
                                               found_already)
                player_found_word = player_found_word.join(found_already)
                break
        display_word(word_picked, found_already)
        print("You have {} guesses left to guess the word and win.".
              format(8 - guess_count))
        if is_word_complete(word_picked, found_already) and guess_count < 9:
            print("Congratulations, you guessed the word and won the game.")
            break
        if guess_count == 8:
            print("Sorry, your allowed guesses has been exceeded.  "
                  "You lost the game.")
            print("The word to guess was {}.".format(word_picked))
        print()
        guess_count += 1
