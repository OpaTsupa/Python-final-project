import random
import re
from hangman_picture import hangman_picture


class Hangman:
    def __init__(self, file_with_words):
        self.words = self._load_words(file_with_words)
        self.possible_lengths = sorted(set(len(word) for word in self.words))
        self.max_length = len(max(self.words, key=len))
        self.min_length = len(min(self.words, key=len))
        self.used_words = []

    def _load_words(self, file_with_words):
        with open(file_with_words, "r", encoding="utf-8") as file:
            return tuple(map(str, file.read().split()))

    def _get_wanted_length(self):
        while True:
            try:
                wanted_length = int(
                    input(
                        f"Введите желаемую длину слова от {self.min_length} до"
                        f" {self.max_length}: "
                    )
                )
                if wanted_length == 0:
                    return None
                if wanted_length in self.possible_lengths:
                    return wanted_length
                print(
                    f'Недопустимая длина. Возможные варианты: {", ".join(map(str, self.possible_lengths))}'
                )
            except ValueError:
                print("Некорректный ввод. Введите число.")

    def _choose_word(self):
        wanted_length = self._get_wanted_length()
        if wanted_length is None:
            return None

        wanted_length_word = [
            word
            for word in self.words
            if len(word) == wanted_length and word not in self.used_words
        ]

        if wanted_length_word:
            word = random.choice(wanted_length_word)
            self.used_words.append(word)
            return word
        print("\nНовых слов такой длины больше нет, все отгаданы!\n")
        return self._prompt_new_length()

    def _prompt_new_length(self):
        choice = input(
            "Вы хотите попробовать отгадать слово другой " "длины? (да\нет) \n"
        )
        while choice not in ("да", "нет"):
            choice = input('Введите "да" или "нет") \n')
        return self._choose_word() if choice == "да" else None

    def _guess_word(self):
        word_for_game = self._choose_word()
        if not word_for_game:
            print("Спасибо за игру!")
            print(f'Отгаданные слова: {", ".join(self.used_words)}')
            return

        wrong_answers = 0
        max_wrong_answers = len(hangman_picture) - 1
        hidden_word = ["_"] * len(word_for_game)
        used_letters = []

        print("\nНачнем игру!")
        print(f'Попробуйте угадать слово: {"".join(hidden_word)}\n')
        print('Для выхода из игры введите "выход".\n')

        while wrong_answers <= max_wrong_answers and hidden_word != list(
            word_for_game
        ):

            if len(used_letters) != 0:
                print(f"Буквы, которые вы пробовали {used_letters}\n")

            guess_letter = input("Ваша буква: ").lower()

            if guess_letter == "выход":
                secret = input(
                    'Хотите увидеть слово полностью? (да\нет)\n').lower()
                if secret == 'да':
                    print(f'\nЗагаданное слово: {word_for_game}')
                    print("Выход из игры.")
                    return
                elif secret == 'нет':
                    print("Выход из игры.")
                    return
                else:
                    continue
            if len(guess_letter) != 1 or not re.match("^[а-я]$", guess_letter):
                print("Введите одну русскую букву.")
                continue
            if guess_letter in used_letters:
                print("Вы уже пробовали эту букву.")
                continue

            used_letters.append(guess_letter)

            if guess_letter in word_for_game:
                position = [
                    i for i, l in enumerate(word_for_game) if l == guess_letter
                ]
                for num in position:
                    hidden_word[num] = guess_letter
                print("".join(hidden_word))
            else:
                wrong_answers += 1
                print(f"Буквы {guess_letter} в слове нет.\n")
                print(hangman_picture[wrong_answers])
                print(f"Осталось попыток: {max_wrong_answers - wrong_answers}")
                print("".join(hidden_word))

            if wrong_answers == max_wrong_answers:
                print("Вы проиграли!")
                print(f"Загаданным словом было: {word_for_game}\n")
                self._continue_game()

            if hidden_word == list(word_for_game):
                print(f"Вы отгадали слово! Вот оно: {''.join(hidden_word)}\n")
                self._continue_game()

    def _continue_game(self):
        answer = input("\nХотите сыграть еще раз?")
        while answer not in ("да", "нет"):
            answer = input("Введите да или нет: ").lower()
        if answer == "да":
            self._guess_word()
        elif answer == "нет":
            print("\nСпасибо за игру!")
            print(f"Отгаданные слова: {', '.join(self.used_words)}\n")

    def play_game(self):
        self._guess_word()


test = Hangman("words.txt")
test.play_game()
