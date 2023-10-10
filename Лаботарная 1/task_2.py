# TODO Найдите количество книг, которое можно разместить на дискете
number_pages = 100
number_line = 50
number_symbol = 25
number_byte = 4
total_byte = number_pages * number_line * number_symbol * number_byte
volume_disk = 1.44
volume_disk_in_byte = 1024 *  1024 * volume_disk
count_book_in_disk = int(volume_disk_in_byte /total_byte)
print("Количество книг, помещающихся на дискету:", count_book_in_disk)
