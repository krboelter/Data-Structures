array = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
new_array = []

for i in array:
    if i % 3 == 0:
        new_array.append(i)
        
print(new_array)
