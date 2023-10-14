# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines = 50
symbols = 25
symbol_byte = 4
book_in_byte = pages * lines * symbols * symbol_byte
disk_volume_in_byte = 1.44 * (1024 ** 2)
book_in_disk = disk_volume_in_byte // book_in_byte

print("Количество книг, помещающихся на дискету:", int(book_in_disk))
