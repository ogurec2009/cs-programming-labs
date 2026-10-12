document_code = input()

print(f"Категория: {document_code[:3]}")
print(f"Год: {document_code[4:8]}")
print(f"Номер: {document_code[9:]}")
print(f"Обратный номер: {document_code[12:8:-1]}")

