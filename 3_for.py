"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

from random import randint


def mean(scores):
  return round(sum(scores)/len(scores), 2), len(scores)


def rand_scores(quantity, start=2, end=5):
    return list(randint(start, end) for i in range(quantity))


def main():
    common_length = 0
    common_score = 0
    for school_class in school:
      mean_score, length  = mean(school_class["scores"])
      common_length += length 
      common_score += mean_score * length
      print(f'Cредний балл по {school_class["school_class"]} классу: {mean_score}')
    print('-' * 30)
    print(f'Cредний балл по всей школе: {round(common_score/common_length, 2)}')


if __name__ == "__main__":
    school = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '4б', 'scores': rand_scores(6)},
      {'school_class': '5a', 'scores': rand_scores(7)},
      {'school_class': '5б', 'scores': rand_scores(9)},
      {'school_class': '6a', 'scores': rand_scores(6)},
      {'school_class': '6б', 'scores': rand_scores(6)},
      {'school_class': '7a', 'scores': rand_scores(12,3)},
      {'school_class': '8а', 'scores': rand_scores(11)},
      {'school_class': '8б', 'scores': rand_scores(7)},
      {'school_class': '8в', 'scores': rand_scores(14)},
      {'school_class': '9a', 'scores': rand_scores(15)},
      {'school_class': '9б', 'scores': rand_scores(16)},
    ]

    main()
