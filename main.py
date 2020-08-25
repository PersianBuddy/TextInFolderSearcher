import os
# get desired text from user
user_text = input("Please enter your desired text to search here: ")

current_directory = os.path.curdir
directorys_list = os.listdir(current_directory)
files_with_text = f'These files contains the word "{user_text}":\n\n'

# search all ".txt" files inside current directory
for directory_name in directorys_list:
    if directory_name.endswith(".txt"):
        tmp_directory = os.path.join(current_directory, directory_name)
        text_file = open(tmp_directory, 'r')
        if user_text.lower() in text_file.read().lower():
            files_with_text += f'File name:\tsample.txt\n File Direcotry: \t{current_directory}\n\n'

# return Files and location where text had been found
print(files_with_text)
