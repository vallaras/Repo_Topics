search_text = "self.insert_query(study, subject, payload)"
replace_text = "# self.insert_query(study, subject, payload)"
with open(r'Hash_task.py', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
with open(r'Hash_task.py', 'w') as file:
    file.write(data)
print(data)