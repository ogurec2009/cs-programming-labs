phone_number = input()

clean_phone_number = ""
for sym in phone_number:
    if sym.isdigit():
        clean_phone_number += sym

print(clean_phone_number)
