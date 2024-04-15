#!/usr/bin/python3

try:
    with open('my_file.txt', 'w') as f:
        f.write("This is line 1.\n")
        f.write("This is line 2.\n")
        f.write("The last line.\n")
except PermissionError:
    print("Access denied")
finally:
    print("File created successfully")

# File Reading and Display
try:
    with open("my_file.txt", "r") as f:
        print("Content of the file:")
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found")
finally:
    print()
    print("File has been read successfully")

#File Appending
try:
    with open("my_file.txt", "a") as f:
        f.write("Append line 1.\n")
        f.write("Append line 2.<n")
        f.write("Append last line.\n")
except PermissionError:
    print("Access denied")
finally:
    print("File appending completed.")
