import re
import getpass
import string


def get_password_from_user(minimum_password_length):
    return getpass.getpass(
        'Enter a password (minimum length {} is required): '.format(minimum_password_length)
    )


def load_blacklisted_words(filename):
    with open(filename) as file:
        return file.read().splitlines()


def character_is_present(case, password):
    return max(
        map(lambda x: case(x), password)
    )


def has_blacklisted_words(password, blacklisted_words):
    return password not in blacklisted_words


def has_special_character(password):
    regex = re.compile('[{}]'.format(
        re.escape(string.punctuation))
    )
    special_character_is_present = re.search(
        regex,
        password
    )
    return 0 if special_character_is_present is None else 3


def has_lower_and_upper_case(password):
    upper_is_present = character_is_present(str.islower, password)
    lower_is_present = character_is_present(str.isupper, password)
    return upper_is_present + lower_is_present


def has_digit(password):
    digit_is_present = character_is_present(str.isdigit, password)
    return digit_is_present * 2


def has_required_length(password):
    return len(password) > 10


def get_password_strength(password, black_listed_words, minimum_password_length):
    current_score = 1

    if len(password) < minimum_password_length:
        return current_score

    evaluations = [
        has_required_length(password),
        has_digit(password),
        has_lower_and_upper_case(password),
        has_special_character(password),
        has_blacklisted_words(password, black_listed_words)
    ]
    return current_score + sum(evaluations)


if __name__ == '__main__':

    minimum_password_length = 6

    try:
        blacklisted_words = load_blacklisted_words('blacklist.txt')
    except FileNotFoundError:
        blacklisted_words = []
        print('Cannot open file with blacklisted words. Checking for blacklisted words will be skipped.')

    password_to_evaluate = get_password_from_user(minimum_password_length)

    security_score = get_password_strength(
        password_to_evaluate,
        blacklisted_words,
        minimum_password_length
    )
    print('Your password security score is {}'.format(security_score))
