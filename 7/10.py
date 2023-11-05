import re
with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
matches = re.findall(r'[A-Z][a-z]*', data)
snake_case_data = '_'.join([match.lower() for match in matches])
with open("newRow.txt", "w", encoding="utf-8") as file:
    file.write(snake_case_data)
