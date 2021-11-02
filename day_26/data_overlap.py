file1 = open("./data/file1.txt")
numbers_file1 = file1.readlines()
# print(numbers_file1)
file2 = open("./data/file2.txt")
numbers_file2 = file2.readlines()
# print(numbers_file2)

result = [int(n) for n in numbers_file1 if n in numbers_file2]

file2.close()
file1.close()
# Write your code above 👆

print(result)
