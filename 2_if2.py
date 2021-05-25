"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры 
  и выводя на экран результаты

"""


     
def string_comparison(first_sring, second_string):
    if not (isinstance(first_sring, str) and isinstance(second_string, str)):
      return 0
    elif first_sring == second_string:
      return 1
    elif len(first_sring) > len(second_string):
      return 2
    elif first_sring != second_string and second_string.strip() == "learn":
      return 3
    return 'Out of comparison'


def main():
    for values in test_string:
      print('Результат сравнения:', string_comparison(values[0], values[1]))

    
if __name__ == "__main__":
    test_string = [
      [5, 'разные'], 
      ['Если строки разные', 'на экран результаты'], 
      ['разные', True], 
      ['на экран результаты', 'learn'],
      ['на', 'learn'],
      ['abc', 'abc']
    ]

    main()
