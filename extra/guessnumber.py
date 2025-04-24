import random

def generate_number(digit_count):
    first_digit = str(random.randint(1, 9))
    remaining_digits = ''.join(str(random.randint(0, 9)) for _ in range(digit_count - 1))
    print(first_digit + remaining_digits)
    return first_digit + remaining_digits

def count_correct_digits(secret, guess):
    return sum(1 for s, g in zip(secret, guess) if s == g)

def main():
    digit_count = int(input("Хэдэн оронтой байх вэ? (2-9): "))
    secret_number = generate_number(digit_count)

    attempts = 0
    while True:
        guess = input(f"Таны оруулсан {digit_count} оронтой тоог таах: ")
        if len(guess) != digit_count or not guess.isdigit():
            print("Зөвхөн тоон утга оруулна уу.")
            continue
        
        attempts += 1
        correct = count_correct_digits(secret_number, guess)
        print(f"{correct} орон зөв таасан байна.")

        if guess == secret_number:
            print(f"Баяр хүргэе! Та {attempts} үйлдлээр тааллаа.")
            break

if __name__ == "__main__":
    main()