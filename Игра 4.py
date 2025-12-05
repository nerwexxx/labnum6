import random

words = ['компьютер', 'программа', 'алгоритм', 'питон', 'программирование', 'виселица']

def play_hangman():
    word = random.choice(words)
    guessed = ['_'] * len(word)
    mistakes = 0
    max_mistakes = 6
    used_letters = []
    
    print("Давайте играть в Виселицу!")
    print(f"Слово состоит из {len(word)} букв")
    
    while mistakes < max_mistakes and '_' in guessed:
        print(f"\nОшибок: {mistakes}/{max_mistakes}")
        print("Слово:", ' '.join(guessed))
        print("Использованные буквы:", ', '.join(used_letters))
        
        letter = input("Введите букву: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введите одну букву!")
            continue
        
        if letter in used_letters:
            print("Вы уже пробовали эту букву!")
            continue
        
        used_letters.append(letter)
        
        if letter in word:
            print("Верно!")
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            print("Нет такой буквы!")
            mistakes += 1
    
    print(f"\nЗагаданное слово: {word}")
    
    if '_' not in guessed:
        print("Поздравляем! Вы угадали слово!")
    else:
        print("Вы проиграли! Попробуйте еще раз.")

if __name__ == "__main__":
    play_hangman()
