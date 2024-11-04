alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where —" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = "\"Would you tell me, please, which way I ought to go from here?\"\n" \
                      "\"That depends a good deal on where you want to get to,\" said the Cat.\n" \
                      "\"I don't much care where ——\" said Alice.\n" \
                      "\"Then it doesn't matter which way you go,\" said the Cat.\n" \
                      "\"—— so long as I get somewhere,\" Alice added as an explanation.\n" \
                      "\"Oh, you're sure to do that,\" said the Cat, \"if you only walk long enough.\""

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = [char for char in alice_in_wonderland if char == "'"]
print("Символи одинарної лапки:", single_quotes)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area

print("Площа Чорного та Азовського морів разом:", total_area, "км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
first_and_second = 250449
second_and_third = 222950
second_warehouse = first_and_second + second_and_third - total_goods
first_warehouse = first_and_second - second_warehouse
third_warehouse = second_and_third - second_warehouse

print("На першому складі:", first_warehouse)

print("На другому складі:", second_warehouse)

print("На третьому складі:", third_warehouse)


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

monthly_payment = 1179
months = 1.5 * 12
total_cost = monthly_payment * months

print("Вартість комп'ютера:", total_cost, "грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

print("Залишок від 8019 / 8:", 8019 % 8)

print("Залишок від 9907 / 9:", 9907 % 9)

print("Залишок від 2789 / 5:", 2789 % 5)

print("Залишок від 7248 / 6:", 7248 % 6)

print("Залишок від 7128 / 5:", 7128 % 5)

print("Залишок від 19224 / 9:", 19224 % 9)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_count = 4
big_pizza_price = 274
medium_pizza_count = 2
medium_pizza_price = 218
juice_count = 4
juice_price = 35
cake_count = 1
cake_price = 350
water_count = 3
water_price = 21
total_cost = (big_pizza_count * big_pizza_price) + \
             (medium_pizza_count * medium_pizza_price) + \
             (juice_count * juice_price) + \
             (cake_count * cake_price) + \
             (water_count * water_price)

print("Загальна вартість замовлення:", total_cost, "грн")


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photos = 232
photos_per_page = 8
pages_needed = (photos + photos_per_page - 1) // photos_per_page

print("Ігорю потрібно сторінок:", pages_needed)


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
fuel_per_100_km = 9
tank_capacity = 48
fuel_needed = (distance / 100) * fuel_per_100_km
refuels_needed = (fuel_needed + tank_capacity - 1) // tank_capacity

print("Для подорожі потрібно:", fuel_needed, "літрів бензину")
print("Заправлятися потрібно:", refuels_needed, "разів")