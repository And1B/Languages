number = input("Give me a number: ")
array = []

for num in number:
    array.append(num)
# array.reverse()
# for number in array:
#     print(number)

res = array[::-1]
print(res)
    