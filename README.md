Title: Python Dictionary Search Engine

* To begin with execution, follow these steps:
	1. Download this repository.
	2. Extract "dictionary.rar"
	3. Execute "dictionary.py" (check line-52 is uncommented, re-comment after execution). Step 3 usually takes some time.
	4. Execute "search-dictionary.py" to perform a search in the dictionary.
* This project is a part of my internship work at KnitArena.

This directory contains 5 important files:
	1. dictionary.rar
	2. dictionary.txt - Extracted from "dictionary.rar"
	3. dictionary.py - Processes data from "dictionary.txt" and writes processed data to "dictionary-in-text-file.txt"
	4. search-dictionary.py - Accesses "dictionary-in-text-file.txt" and queries user input for "meanings"
	5. dictionary-in-text-file.txt - Automatically created when "dictionary.py" is executed. Contains JSON format data with key-value pairs.


* To Generate "dictionary-in-text-file.txt" only, execute "dictionary.py".
* To Search for a word, execute "search-dictionary.py".
* "dictionary.txt" in this repository was manually edited to remove any text other than 'words' and 'meanings'
* For original "dictionary.txt" file, extract "dictionary.rar"
* Unwanted data in "dictionary.txt" is found in the beginning and the end of the file. Deleting this text does not affect the Search Engine.
* Alternatively, "dictionary.txt" can be found online here: "https://www.gutenberg.org/ebooks/29765.txt.utf-8"
	! Web-address could vary over time.