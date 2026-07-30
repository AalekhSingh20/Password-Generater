import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    characters = string.ascii_letters + string.digits + string.punctuation

    password.extend(random.choice(characters) for _ in range(length - 4))
    random.shuffle(password)

    return "".join(password)


def main():
    print("=" * 40)
    print("      PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))
        password = generate_password(length)
        print("\nGenerated Password:", password)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
