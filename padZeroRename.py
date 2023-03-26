import os

# Change this to the directory path containing the files
dir_path = "./out/lesson_2/"

# Loop through all files in the directory
for filename in os.listdir(dir_path):
    # Change this to the file extension of the files you want to rename
    if filename.endswith(".png"):
        file_number = filename.split("image")[1].split(
            ".")[0]  # Extract the number from the file name
        # Pad the number with zeros to 4 digits
        new_number = file_number.zfill(4)
        # Replace the old number with the padded number in the file name
        new_filename = filename.replace(file_number, new_number)
        os.rename(dir_path + filename, dir_path +
                  new_filename)  # Rename the file
