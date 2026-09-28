document_code = input()

category, year, doc_id = document_code.split("-")

doc_id_backwards = doc_id[::-1]

print(f"Категория: {category}\nГод: {year}\nНомер: {doc_id}\nОбратный номер: {doc_id_backwards}")

