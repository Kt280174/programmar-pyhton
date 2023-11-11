# TODO решите задачу
import json


def task() -> float:
    filename = 'input.json'
    with open(filename) as file:
        data = json.load(file)
    list_values = [item['score'] * item['weight'] for item in data]
    return round(sum(list_values), 3)


print(task())
