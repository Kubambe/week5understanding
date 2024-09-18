# file_handling_assignment.py

def create_file():
    print("Let's create a new file and write some content to it!")
    with open('my_file.txt', 'w') as file:
        print("Enter three lines of text to write to 'my_file.txt':")
        for i in range(1, 4):
            line = input(f"Line {i}: ")
            file.write(line + '\n')
    print("\nFile 'my_file.txt' created and initial content written.")

def read_file():
    print("\nReading the contents of 'my_file.txt':")
    with open('my_file.txt', 'r') as file:
        content = file.read()
    print(content)

def append_to_file():
    print("\nLet's add more content to the file!")
    with open('my_file.txt', 'a') as file:
        print("Enter three additional lines of text to append:")
        for i in range(1, 4):
            line = input(f"Additional Line {i}: ")
            file.write(line + '\n')
    print("\nAdditional lines appended to 'my_file.txt'.")

def main():
    print("Welcome to the File Handling Fun!\n")
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read file again to show appended content
    print("\nThanks for using the File Handling Fun script!")

if __name__ == "__main__":
    main()
