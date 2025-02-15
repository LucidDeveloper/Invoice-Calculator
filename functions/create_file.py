# create file in current working directory

def create_file(file_path, file):
    try:
        # Attempt to create a file
        file = open(file_path, "x")
        file.close()
        print(f"\nNew File Created.")
        return False # File does not exist
    except FileExistsError:
        # If the file already exists, print a message
        print(f"\nFile already exists.")
        return True # File exists