""" This is a python script which can edit its script and add
a new key and value in a dictionary present in it."""

__author__ = "Swastik Saha"

import os  # Importing os module

# Declaring the dictionary in variable dict_editable
dict_editable = {'apple': 'a fruit'}

inp_key = fr"{input('Enter a key for dictionary : ')}"           # Taking input for new key in dictionary
inp_val = fr"{input('Enter the value for that key : ')}"         # Taking input for new value of the entered key


filename = os.path.basename(__file__)  # Declaring variable filename which contains the name of this script
f_obj = open(filename, "r")

file_lines = f_obj.readlines()
f_obj.close()
dict_var_declare = "dict_editable = "   # This is to declare the dictionary in dict_editable variable
dict_line = 8  # Declaring the dict_line variable
# Finding the index of the line which contains the dictionary which is to be edited
for index in range(len(file_lines)):
    if file_lines[index].startswith(dict_var_declare):
        dict_line = index   # Storing the found index in dict_line variable
        break

old_dict = eval(file_lines[dict_line].replace(dict_var_declare, ""))  # Storing old dictionary in variable old_dict
old_dict[inp_key] = inp_val  # Adding new key and value in old dictionary
new_dict = str(old_dict)     # Typecasting the dictionary explicitly to string to write in file
file_lines[dict_line] = dict_var_declare + new_dict + "\n"  # Changing the dictionary in specific line of file_lines

# Changing the script of the main file
new_f_obj = open(filename, "w")
for line in file_lines:
    new_f_obj.write(line)

new_f_obj.close()  # Closing the main file
