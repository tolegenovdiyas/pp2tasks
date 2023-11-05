import re
with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()
edited_data = re.sub(r'(?<=[a-z])([A-Z])', r' \1', data)
with open("newRow.txt", "w", encoding="utf-8") as file:
    file.write(edited_data)
