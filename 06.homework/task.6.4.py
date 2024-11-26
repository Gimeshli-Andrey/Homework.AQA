numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even = 0
for number in numbers:
    if number % 2 == 0:
        sum_of_even += number
print("Сума усіх парних чисел:", sum_of_even)
