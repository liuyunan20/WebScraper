number = int(input())
bytes_number = number.to_bytes(5, byteorder='little')
number_from_bytes = int.from_bytes(bytes_number, 'little')
print(number == number_from_bytes)  # <-- expected to be True!
