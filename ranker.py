# Task for Playrix interview
# @dimaryst
class Ranker:
    def __init__(self):
        # Editable by method only
        self.__average_rank = None
        self.__dictionary = dict

    def set_dict(self, dictionary):  # Метод для получения словаря
        self.__dictionary = dictionary
        self.get_average_rank()

    def get_average_rank(self):
        t_list = self.__dictionary
        t_list = list(t_list.items())
        counter = 0
        points_sum = 0
        for item in t_list:  # count items and sum
            points_sum += item[1]
            counter += 1
        self.__average_rank = points_sum / counter  # save average rank / запоминиаем средний рейтинг
        return self.__average_rank

    def get_ranking_names(self):
        ranking_names = list()
        t_list = self.__dictionary
        t_list = list(t_list.items())
        t_list.sort(key=lambda i: i[1], reverse=True)  # Reverse sort for new list with names / Сортировка по значению
        for item in t_list:
            ranking_names.append(item[0])  # fill list with sorted names
        return ranking_names

