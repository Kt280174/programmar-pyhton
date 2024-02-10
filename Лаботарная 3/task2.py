# TODO Напишите функцию find_common_participants
def find_common_participants(participants1, participants2, symbol=','):
    common = list(set(participants1.split(symbol)).intersection(participants2.split(symbol)))
    common.sort()
    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
