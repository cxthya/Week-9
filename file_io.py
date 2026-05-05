'''
Cinthya Calderon-Hernandez
CSMC 111
Spring 2026
'''

#Used ChatGPT to write code

# file_io.py

# Part 1: Read and Print a File
try:
    with open("input.txt", "r") as file:
        content = file.read()
        print("Contents of input.txt:")
        print(content)
except FileNotFoundError:
    print("Error: input.txt was not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")


# Part 2: Create a New File and Write User Input
try:
    user_input = input("Enter text to save to file: ")

    with open("output.txt", "w") as file:
        file.write(user_input)

    print("Your text has been written to output.txt")

except Exception as e:
    print(f"An error occurred while writing to the file: {e}")


# Part 3: Append to an Existing File
try:
    with open("output.txt", "a") as file:
        file.write("\nHello, World!")

    print("Text has been appended to output.txt")

except Exception as e:
    print(f"An error occurred while appending to the file: {e}")