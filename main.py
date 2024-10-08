# Open a file in write mode, create it if it doesn't exist
file = open("example.txt", "w")
file.write("Hello, this is a test file for file operations practice.\n")
file.write("This is the second line in the file.\n")
file.close()

# Open the file in read mode and read the contents
file = open("example.txt", "r")
content = file.read()
print("File content:")
print(content)
file.close()

# Open the file in append mode and add another line
file = open("example.txt", "a")
file.write("This is an appended line.\n")
file.close()

# Read the file again to see the appended content
file = open("example.txt", "r")
print("Updated file content:")
print(file.read())
file.close()

# Handling file exceptions
try:
    file = open("non_existing_file.txt", "r")
except FileNotFoundError:
    print("File not found. Please check the file path.")
