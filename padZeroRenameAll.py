import os

# Change this to the parent directory path containing the lesson folders
parent_dir = "./out/"

# Loop through all directories and subdirectories
for dirpath, dirnames, filenames in os.walk(parent_dir):
    # Loop through all files in the directory
    for filename in filenames:
        # Change this to the file extension of the files you want to rename
        if filename.endswith(".png"):
            # Extract the number from the file name
            file_number = filename.split("image")[1].split(".")[0]
            # Pad the number with zeros to 4 digits
            new_number = file_number.zfill(4)
            # Replace the old number with the padded number in the file name
            new_filename = filename.replace(file_number, new_number)
            # Rename the file
            os.rename(os.path.join(dirpath, filename),
                      os.path.join(dirpath, new_filename))
