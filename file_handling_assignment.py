
try:

    with open('my_file.txt', 'w') as file:
        file.write("This is the first line of the file.\n")
        file.write("Here is the second line, which includes a number: 123\n")
        file.write("Finally, the third line is here.\n")
    print("File created and initial content written successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while creating or writing to the file: {e}")

finally:
    print("File creation section completed.")

try:

    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nFile Content:\n")
        print(content)

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while reading the file: {e}")

finally:
    print("File reading section completed.")


try:
   
    with open('my_file.txt', 'a') as file:
        file.write("Appending a new line to the file.\n")
        file.write("Another line added to the end.\n")
        file.write("Final appended line.\n")
    print("Additional content appended successfully.")

except (FileNotFoundError, PermissionError) as e:
    print(f"Error occurred while appending to the file: {e}")

finally:
    print("File appending section completed.")
