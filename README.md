# Hangman Game (Игра "Виселица")

## Описание

Это текстовая игра "Виселица", написанная на Python. В игре пользователь должен угадывать слова, выбирая буквы по очереди. За каждую неверную попытку отображается часть виселицы, и если количество неверных попыток превышает допустимое, игра заканчивается. Игра предлагает пользователю выбрать длину слова, и из списка слов будет случайным образом выбрано подходящее.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/OpaTsupa/Python-final-project.git

Перейдите в директорию проекта:

    cd \Final project\final_project\hangman\

Убедитесь, что у вас установлен Python 3. Вы можете установить его с официального сайта Python.

Создайте и активируйте виртуальное окружение:

Для Windows:

    python -m venv venv
    venv\Scripts\activate

Для Linux/macOS:

    python3 -m venv venv
    source venv/bin/activate

Установите зависимости:

    pip install -r requirements.txt

Использование

Чтобы запустить игру, выполните следующий скрипт:

    python main.py

Или, если ваш основной файл называется как-то по-другому, запустите его:

    python путь_к_файлу.py

При запуске игры вам будет предложено ввести желаемую длину слова, после чего вы начнете угадывать слово, выбирая по одной букве за раз. Если хотите выйти из игры, введите "выход".
Формат словаря

Игра ожидает файл с текстом, в котором слова разделены пробелами или новой строкой. Пример файла words.txt:

    яблоко
    апельсин
    груша
    банан

Как работает игра?

    Игра начинает с запроса длины слова.
    После выбора длины случайным образом выбирается слово.
    Игрок поочередно вводит буквы, пытаясь угадать слово.
    На экране отображается прогресс отгадывания слова и состояние виселицы, если игрок делает неправильные попытки.
    Если игрок проигрывает (достигнут лимит неверных попыток), игра предлагает начать заново.

Пример игры

    Введите желаемую длину слова от 5 до 7: 6
    Начнем игру!
    Попробуйте угадать слово: _ _ _ _ _ _
    Для выхода из игры введите "выход".
    
    Ваша буква: а
    Буквы а в слове нет.
    
    _ _ _ _ _ _
    Осталось попыток: 5
    
    Ваша буква: о
    _ _ _ о _ _
    ...
    
    Вы отгадали слово! Вот оно: апельсин
    Хотите сыграть еще раз? (да/нет)