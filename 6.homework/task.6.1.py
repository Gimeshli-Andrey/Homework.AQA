user_input = input("Enter the string: ")
unique_characters = set(user_input)
if len(unique_characters) > 10:
    print(True)
else:
    print(False)