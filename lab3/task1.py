document_code = input()

print(f"Категория: {document_code[:3]}\nГод: {document_code[4:8]}\nНомер: {document_code[9:]}\nОбратный номер: {document_code[12:8:-1]}")

