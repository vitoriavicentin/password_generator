import random
import string

def get_random_string(lgth):
    ch = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(ch) for _ in range(lgth))
    return password

def main():
    password_lgth = 8
    random_password = get_random_string(password_lgth)
    print("A Random password is:", random_password)

if __name__ == "__main__":
    main()