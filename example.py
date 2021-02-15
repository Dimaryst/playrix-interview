#!/usr/bin/python3
# Task for Playrix interview
# @dimaryst
from ranker import Ranker
# Example / Пример использования

example_dict_1 = {'A': 5, 'B': 2, 'C': 13, 'D': 11, 'E': 4}
example_dict_2 = {'Alice': 2, 'Bob': 8, 'Chad': 2, 'Dean': 3}

obj = Ranker()  # New object / Создаем объект
obj.set_dict(example_dict_1)  # Add dict to object / Добавляем в объект класса Ranker словарь
print("Dict 1")
print(f"Rating: {obj.get_ranking_names()}")
print(f"Average rating: {obj.get_average_rank()}\n")

obj = Ranker()  # New object / Создаем объект
obj.set_dict(example_dict_2)  # Add dict to object / Добавляем в объект класса Ranker словарь
print("Dict 2")
print(f"Rating: {obj.get_ranking_names()}")
print(f"Average rating: {obj.get_average_rank()}")

