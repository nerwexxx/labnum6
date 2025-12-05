import random

def play_game():
    min_num = 0
    max_num = 100
    secret = random.randint(min_num,max_num)
    print(f"Я загадал число от {min_num} до {max_num}. Угадай:)")

    attemps = 0
    while True:
        try:
            guess = int(input("Твоя догадка"))
            attemps+=1
            if guess < secret:
                print("бери больше!!")
            elif guess > secret:
                print("бери меньше!!")
            else:
                print(f"Угадал! Ай лев! Ай тигр! Ты угадал с {attemps} попытки")
                break
        except ValueError:
            print("Число нормально введи")
play_game()
