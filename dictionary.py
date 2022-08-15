import json
import os
import sys

def processRawDictionary():

    # ACCESS RAW DATA
    with open(os.path.join(sys.path[0], "dictionary.txt"), "r") as dictionary:
        lines = dictionary.readlines()
    # Store raw data in 'lines'


    py_dict = {}
    # Declare Empty Dictionary
    # This will store the (key:value) pair

    # DATA PROCESSING
    for i in range(len(lines)):
        print(i)
        # Prints index. Just to ensure if program is executing...
        if lines[i].isupper():
            # All key words are in upper case, hence they become the key for the dictionary data structure
            key = lines[i].replace("\n", "")
            meaning = ""
            # 'meaning' is the value for its respective key
            for j in range(i + 1, len(lines)):
                # Start loop from the line succeeding 'key'
                if lines[j].isupper():
                    # Continue loop until another upper case string is found
                    break
                else:
                    # Else keep appending consequent strings to 'meaning'
                    meaning = meaning + lines[j]
            if key not in py_dict:
                # If 'key' does not exist, create the 'key'
                # Its values are stored in a list
                # There could be homophones in the dictionary
                py_dict.update({key: [meaning]})
            else:
                # If a 'key' is repeated, append the new meaning to existing list
                py_dict[key].append(meaning)

    # STORE PROCESSED DATA
    with open(os.path.join(sys.path[0], "dictionary-in-text-file.txt"), "w") as actual_dict:
        actual_dict.write(json.dumps(py_dict))

    print("DATA PROCESSING COMPLETE")
    # Now we have a (key:value) pair dictionary
    # This is stored in a text file in JSON format
    # This file will accessed by 'search-dictionary.py' file to provide query results

# processRawDictionary()

# Uncomment line 52 if you want to generate "dictionary-intext-file.txt" in JSON Format only
# Comment the line 52 after generating the file
# If line 52 is not commented while executing "search-dictionary.py"
#           the above functions will be called every time