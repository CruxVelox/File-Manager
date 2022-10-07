#Sentence Analyzer 0.1.1, Idea and Programming by Cruxvelox
#This is what does the user input
print("Sentence Analyzer v0.1.1")
input = input("Sentence to analyze: ")
#Defining lowercase letters variable and setting it to 0
lowercase_occurrences=0
#Doing the same thing here: defining uppercase letters variable and setting it to 0
uppercase_occurrences=0
#Defining the word count variable
word_list = input.split()
words_count = len(word_list)
#Taking uppercase and lowercase variables to life
for i in input:
      if(i.islower()):
            lowercase_occurrences=lowercase_occurrences+1
      elif(i.isupper()):
            uppercase_occurrences=uppercase_occurrences+1
#Defining input character count variable
input_length = len(input)

#Setting a minimum limit of 0 for the input string
if input_length == 0:
	print("\33[101m\33[1m\33[5m[FATAL WARNING] \33[0m\33[4mYour sentence has nothing in it. Please restart the program.\33[0m")
print("\33[44m\33[1m  [INFO]  \33[0m\33[4m\33[7m  Analyzing Sentence...\33[0m")
#Telling the program to print a warning when it reaches its maximum limit (looks so small)
if input_length == 4095:
	print("\33[1m\33[7;49;93m  [WARNING]  \33[0m\33[4m  You reached the limit\ncharacter count for the program. It could be small, but if you were trying to count the characters, words or whatever of an e-mail...")
print("\33[100mSentence Length in Characters: \33[1m\33[42m", input_length, "\33[0m")
print("\33[100mUppercase Letters in Sentence: \33[1m\33[42m", uppercase_occurrences, "\33[0m")
print("\33[100mLowercase Letters in Sentence: \33[1m\33[42m", lowercase_occurrences, "\33[0m")
print("\33[100mWords Count in Sentence:       \33[1m\33[42m", words_count, "\33[0m")
