"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
import datetime
import os


def get_dictionary():
  questions_and_answers = {
      "Как дела?": "Хорошо!", 
      "Что делаешь?": "Программирую",
      "Сколько время?": datetime.datetime.now().time(),
      "День": datetime.datetime.now().date(),
      "ОС": os.name,
      "Текущая деректория": os.getcwd(),
      "Содержимое": '\n'.join(map(str, os.listdir()))
      }
  return questions_and_answers


def ask_user():
    while question := input('Пользователь: '):
      questions_and_answers = get_dictionary()
      if question in questions_and_answers:
        print(f'Программа: {questions_and_answers[question]}')
      else:
        break


if __name__ == "__main__":
    ask_user()
