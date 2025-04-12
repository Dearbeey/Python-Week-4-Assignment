def modify_content(content):
    lines = content.splitlines()
    numbered_lines = [f"{idx +1}: {line}" for idx, line in enumerate(lines)]
    return "\n".join(numbered_lines)
def read_and_write_file():
    filename = input("Enter the file name: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("file read successfully")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    except IOError:    
        print(f"Error: Could not read the file '{filename}'.")
        return
    modified_content = modify_content(content)
    new_filename = f"modified_{filename}"
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Modified content written to '{new_filename}'")
    except IOError:
        print(f"Error: Could not write to the file '{new_filename}'.")
        return
    
read_and_write_file()