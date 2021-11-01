numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
print(numbers)
print(new_list)

name = 'Angela'
new_name = [letter for letter in name]
print(new_name)

new_range = [n*2 for n in range(1, 5)]
print(new_range)

range_list = [n for n in range(1, 5)]
print(range_list)
range_list = [n ** 2 for n in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Bo"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
