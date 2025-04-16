import random

secret_number = random.randint(1, 20)
attempts = 5

print("Я загадал число от 1 до 20. У тебя 5 попыток угадать его!")

for attempt in range(1, attempts + 1):
    print(f"Попытка {attempt}. Осталось попыток: {attempts - attempt + 1}")
    guess = int(input("Твоя догадка: "))
    
    if guess == secret_number:
        print(f"Поздравляю! Ты угадал число {secret_number}!")
        break
    elif guess < secret_number:
        print("Мое число больше.")
    else:
        print("Мое число меньше.")
else:
    print(f"Ты исчерпал все попытки. Я загадал число {secret_number}.")