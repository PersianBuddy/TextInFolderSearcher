import os
# get desired text from user
user_text = input("Please enter your desired text to search here: ")

directorys_list = [os.path.abspath(os.path.curdir)]
files_with_text = f'These files contains the word "{user_text}":\n\n'

# search all ".txt" files inside current directory
while directorys_list:
    current_directory = directorys_list.pop()
    direcoty_content = os.listdir(current_directory)
    for directory_name in direcoty_content:
        if directory_name.endswith(".txt"):
            file_direcoty = os.path.join(current_directory, directory_name)
            text_file = open(file_direcoty, 'r')
            if user_text.lower() in text_file.read().lower():
                files_with_text += f'File name:\t{directory_name}\n File Direcotry: \t{current_directory}\n\n'
        elif os.path.isdir(os.path.join(current_directory, directory_name)):
            directorys_list.append(os.path.join(current_directory, directory_name))

# return Files and location where text had been found
print(files_with_text)
