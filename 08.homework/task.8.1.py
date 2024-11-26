def calculate_sum_from_string(numbers_string):
    try:
        numbers = [int(num) for num in numbers_string.split(',')]
        return sum(numbers)
    except ValueError:
        return "I can't do it!"

string_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

results = []
for string in string_array:
    result = calculate_sum_from_string(string)
    results.append(result)

for res in results:
    print(res)