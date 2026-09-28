raw_input = input()

print(f"Длина: {len(raw_input)}")
print(f"Только буквы: {raw_input.isalpha()}")
print(f"Только цифры: {raw_input.isdigit()}")
print(f"Буквенно-цифровая: {raw_input.isalnum()}")
print(f"Содержит дефис: {raw_input.find("-") > -1}")
