import sys
import re
import getpass


def get_password_from_user():
    return getpass.getpass('Enter a password (minimum length 6 is required): ')


def read_file(filename):
    with open(filename) as file:
        return file.read()


def character_is_present(case, password):
    return max(
        map(lambda x: case(x), password)
    )


def evaluate_has_blacklisted_words(password, blacklisted_words):
    if blacklisted_words is None:
        return 0
    list_of_blacklisted_words = re.findall("\w+", blacklisted_words)
    for word in list_of_blacklisted_words:
        if password.find(word) > -1:
            return 0
    return 1


def evaluate_special_character(password):
    special_character_is_present = re.search(
        "[$ & +,:;=?@  # |'<>.^*()%!-]",
        password
    )
    return 0 if special_character_is_present is None else 3


def evaluate_has_lower_and_upper_case(password):
    upper_is_present = character_is_present(str.islower, password)
    lower_is_present = character_is_present(str.isupper, password)
    return upper_is_present + lower_is_present


def evaluate_has_digit(password):
    digit_is_present = character_is_present(str.isdigit, password)
    return 2 if digit_is_present else 0


def evaluate_length(password):
    return 1 if len(password) > 10 else 0


def get_password_strength(password, black_listed_words):
    current_score = 1

    if len(password) < 6:
        return current_score

    evaluations = [
        evaluate_length(password),
        evaluate_has_digit(password),
        evaluate_has_lower_and_upper_case(password),
        evaluate_special_character(password),
        evaluate_has_blacklisted_words(password, black_listed_words)
    ]
    return current_score + sum(evaluations)


if __name__ == "__main__":
    try:
        blacklisted_words = read_file("blacklist.txt")
    except FileNotFoundError:
        blacklisted_words = None
        print("Cannot open file with blacklisted words. Checking for blacklisted words will be skipped.")

    password_to_evaluate = get_password_from_user()

    security_score = get_password_strength(
        password_to_evaluate,
        blacklisted_words
    )
    print("Your password security score is {}".format(security_score))
