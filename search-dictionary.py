import json
import os
import sys
import dictionary as dProcess
# In "dictionary.py", check if line 52 is commented.
# Uncommented line 52 can cause unnecessary usage of resources

# CHECK IF PROCESSED DATA EXISTS
file_exists = os.path.exists(os.path.join(
    sys.path[0], "dictionary-in-text-file.txt"))


if not file_exists or os.stat(os.path.join(sys.path[0], "dictionary-in-text-file.txt")).st_size == 0:
# If 'file does not exist' or 'dictionary-in-text-file.txt' is empty, execute processRawDictionary()
    print("Could not find processed dictionary...")
    print("Trying to process raw dictionary, this might take some time...")
    dProcess.processRawDictionary()

# ACCESS PROCESSED DATA
with open(os.path.join(sys.path[0], "dictionary-in-text-file.txt"), "r") as actual_dict:
    dictionary = json.load(actual_dict)


print("--------------Welcome to Dictionary--------------\n")
user_input = input("Enter Your Query: ")

# Query convert to upper case
upper_user_input = user_input.upper()

if upper_user_input in dictionary:
    print("You Entered: ", upper_user_input)
    for i in range(len(dictionary[upper_user_input])):
    # Iterate through the 'list' of 'key' and display all meanings
        print(dictionary[upper_user_input][i])
elif upper_user_input not in dictionary:
    print("\n!!! Could not find: ", upper_user_input)
    print("Here are some similar word(s)...\n")
    sub_keys = [key for key in dictionary.keys() if upper_user_input in key]
    for keys in sub_keys:
        print(keys, "\n")
        for i in range(len(dictionary[keys])):
        # Iterate through the 'list' of all alternate 'keys' and display all meanings
            print(dictionary[keys][i])

# Lines 36 through 43 are executed if query is not found in the dictionary
# It checks for the entered query in all keys
# If entered query is a substring of any key, that key is stored in 'sub_keys' list
# Then display all possible alternate words and their meanings
