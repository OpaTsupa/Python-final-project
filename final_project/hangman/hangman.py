import random

class Hangman:
    def __init__(self, file_with_words):
        self.words = self._load_words(file_with_words)
        self.possible_lengths = sorted(set(len(word) for word in self.words))
        self.max_length = len(max(self.words, key=len))
        self.min_length = len(min(self.words, key=len))
        self.used_words = []

    def _load_words(self,file_with_words):
        with open(file_with_words, 'r', encoding='utf=8') as file:
            return tuple(map(str, (file.read().split())))

    def _get_wanted_length(self):
        while True:
            try:
                wanted_length = int(input(
                    f'Введите желаемую длину слова от {self.min_length} до'
                    f' {self.max_length}: '
                ))
                if wanted_length == 0:
                    return 0
            except ValueError:
                print(
                    'Некорректный ввод. Введите число. Для завершения игры '
                    'введите 0.'
                )
                continue
            if wanted_length not in self.possible_lengths:
                print(
                    f'Слова указанной длинны нет в базе. Допустимая длина '
                    f'слов: '
                    f' {', '.join(map(str, self.possible_lengths))}'
                )
                continue
            return wanted_length


    def _choose_word(self, wanted_length):
        wanted_length_words = [word for word in self.words if len(word) ==
                               wanted_length and word not in self.used_words]

        if wanted_length_words:
            word = random.choice(wanted_length_words)
            self.used_words.append(word)
            return word
        else:
            print('Новых слов такой длинны больше нет, все отгадано!')
            print('Спасибо за игру!')
            return f'Отгаданные слова: {', '.join(self.used_words)}'

    def _choose_word_for_game(self):
         self._choose_word(self._get_wanted_length())
