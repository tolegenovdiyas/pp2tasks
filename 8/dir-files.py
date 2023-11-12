#1
'''
import os
def list_items(path):
    dir = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)

    return dir, files, all_items
def main():
    path = input("Enter the path: ")
    directories, files, all_items = list_items(path)
    print("\nDirectories:", directories)
    print("\nFiles:", files)
    print("\nAll Directories and Files:", all_items)
if __name__ == "__main__":
    main()
'''
#2
'''
import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable
def main():
    path = input("Enter the path: ")
    exists, readable, writable, executable = check_path_access(path)
    print("\nPath exists:", exists)
    print("Readable:", readable)
    print("Writable:", writable)
    print("Executable:", executable)
if __name__ == "__main__":
    main()
'''
#3
'''
import os
def analyze_path(path):
    if os.path.exists(path):
        filename, dir = os.path.basename(path), os.path.dirname(path)
        return True, filename, dir
    else:
        return False, None, None
def main():
    path = input("enter the path: ")
    exists, filename, dir = analyze_path(path)
    print("\npath exists." if exists else "\npath does not exist.")
    if exists:
        print("filename:", filename)
        print("directory:", dir)
if __name__ == "__main__":
    main()
'''
#4
'''
import os
def count_lines(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    else:
        print(f"File '{file_name}' not found.")
        return -1
def main():
    file_name = "numbers.txt"
    line_count = count_lines(file_name)

    if line_count != -1:
        print(f"\nThe file '{file_name}' has {line_count} lines.")
if __name__ == "__main__":
    main()
'''
#5
'''
def write_list_to_file(file_name, data_list):
    with open(file_name, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')

def main():
    file_name = 'list.txt'
    input_list = input()
    data_list = [item.strip() for item in input_list.split()]

    write_list_to_file(file_name, data_list)
if __name__ == "__main__":
    main()
'''
#6
'''
import string
def generate_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"success {file_name}")
def main():
    generate_files()
if __name__ == "__main__":
    main()
'''
#7
'''
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        content = source.read()
        with open(destination_file, 'w') as destination:
            destination.write(content)
def main():
    source_file = "1file.txt"
    destination_file = "2file.txt"
    copy_file(source_file, destination_file)
if __name__ == "__main__":
    main()
'''
#8
'''
import os

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    else:
        print(f"Error: File '{file_path}' not found.")

def main():
    file_path = input("Enter the path of the file to delete: ")

    if os.access(file_path, os.F_OK):
        delete_file(file_path)
    else:
        print(f"Error: File '{file_path}' not found.")
if __name__ == "__main__":
    main()
'''