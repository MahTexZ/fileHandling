# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with text and numbers: 9876\n")
except Exception as e:
    print("An error occurred while creating the file:", e)

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Permission denied to access 'my_file.txt'.")
except Exception as e:
    print("An error occurred while reading the file:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4 (appended).\n")
        file.write("Appending numbers: 5678\n")
        file.write("Another appended line.\n")
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Permission denied to access 'my_file.txt'.")
except Exception as e:
    print("An error occurred while appending to the file:", e)
finally:
    print("Script execution completed.")
