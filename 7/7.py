import re
with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
def snake_to_camel(match):
    return match.group(1).upper()
camel_data = re.sub(r'_([a-z])', snake_to_camel, data)
with open("newRow.txt", "w", encoding="utf-8") as file:
    file.write(camel_data)
