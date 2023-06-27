import random
import string


def get_random_string(lgth):
    """
    Generate a random password.
    Args:
        ch (str): A string for random letters.
        lgth (int): Password length.
    Returns:
        str: A random password.
    """
    ch = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(ch) for _ in range(lgth))
    return password


def main():
    """
    Principal function to shown random password.
    """
    password_lgth = 8
    random_password = get_random_string(password_lgth)
    print("A Random password is:", random_password)


if __name__ == "__main__":
    main()
