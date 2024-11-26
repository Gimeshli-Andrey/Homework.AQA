adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_count = adwentures_of_tom_sawer.count('h')
print("Кількість літер 'h':", h_count)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
capitalized_words = [word for word in adwentures_of_tom_sawer.split() if word[0].isupper()]
print("Кількість слів з великої літери:", len(capitalized_words))

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_tom_position = adwentures_of_tom_sawer.find('Tom')
second_tom_position = adwentures_of_tom_sawer.find('Tom', first_tom_position + 1)
print("Позиція другого 'Tom':", second_tom_position)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('. ')
print("Речення:", adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3].lower()
    print("Четверте речення у нижньому регістрі:", fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
by_the_time_sentence = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print("Чи є речення, яке починається з 'By the time':", by_the_time_sentence)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
if len(adwentures_of_tom_sawer_sentences) > 0:
    last_sentence_word_count = len(adwentures_of_tom_sawer_sentences[-1].split())
    print("Кількість слів у останньому реченні:", last_sentence_word_count)