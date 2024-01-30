#This Python script automates the task of file organization within a specified directory.
#This script will organize files based on their types (extensions) into separate folders.

import os
import shutil

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to organize files into directories based on their extensions
def organize_files(directory):

    extensions = {
        "txt": "TextFiles",
        "pdf": "PDFs",
        "jpg": "Images",
        "png": "Images",
        "xlsx": "ExcelFiles",

    }

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the file extension
            file_extension = filename.split(".")[-1].lower()
            # Check if the extension exists in the dictionary
            if file_extension in extensions:
                # Create the destination directory if it doesn't exist
                destination_directory = os.path.join(directory, extensions[file_extension])
                create_directory(destination_directory)
                # Move the file to the destination directory
                shutil.move(os.path.join(directory, filename), os.path.join(destination_directory, filename))
                print(f"Moved {filename} to {extensions[file_extension]} folder.")

# Main function
def main():

    target_directory = r"C:\Users\Tharushi Nadeeshani\Desktop\file automation"

    # Organize files in the target directory
    organize_files(target_directory)

if __name__ == "__main__":
    main()
