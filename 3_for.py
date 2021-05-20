"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

from random import randint


def mean(score_list):
  return round(sum(score_list)/len(score_list), 2), len(score_list)


def rand_list(quantity, start=2, end=5):
    return list(randint(start, end) for i in range(quantity))


def main():
    common_length=0
    common_score=0
    for school_class in school:
      mean_list = mean(school_class["scores"])
      common_length += mean_list[1] 
      common_score += mean_list[0] * mean_list[1]
      print(f'Cредний балл по {school_class["school_class"]} классу: {mean_list[0]}')
    print('-' * 30)
    print(f'Cредний балл по всей школе: {round(common_score/common_length, 2)}')


if __name__ == "__main__":
    school = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '4б', 'scores': rand_list(6)},
      {'school_class': '5a', 'scores': rand_list(7)},
      {'school_class': '5б', 'scores': rand_list(9)},
      {'school_class': '6a', 'scores': rand_list(6)},
      {'school_class': '6б', 'scores': rand_list(6)},
      {'school_class': '7a', 'scores': rand_list(12,3)},
      {'school_class': '8а', 'scores': rand_list(11)},
      {'school_class': '8б', 'scores': rand_list(7)},
      {'school_class': '8в', 'scores': rand_list(14)},
      {'school_class': '9a', 'scores': rand_list(15)},
      {'school_class': '9б', 'scores': rand_list(16)},
    ]

    main()
