users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
dict_ = {'Общее количество': 0, 'Уникальные посещения': 0}
number_users = len(users)
unique_users = set(users)
number_unique_users = len(unique_users)
dict_["Общее количество"] = number_users
dict_["Уникальные посещения"] = number_unique_users
print(dict_)
