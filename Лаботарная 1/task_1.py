numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(len(numbers)):
    if numbers[i] == None:
        numbers[i] = 0
        k = i
sum_of_numbers = sum(numbers)
count_numbers = len(numbers)
numbers[k] = sum_of_numbers/count_numbers
print("Измененный список:", numbers)
