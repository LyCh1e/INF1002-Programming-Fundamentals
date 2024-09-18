r'''
Task Description:
In this task, you are going to design one program to check the popular characters
in a given string. You need to write one program to calculate the top 5 most 
frequent characters. The following are some hints that may help you design this program. 
	. String has a cool function that you can use to return a copy of the string 
     in which all case-based characters have been lowercased. 
	. To get the top 5 most frequent characters after sorting them, you need to 
     extract all the characters first and figure out one way to calculate the frequency 
     of each character. Then select the top 5 characters. 
	. The output must in the descending order of character frequency. If there are 
     characters with the same frequency, they must be printed in ascending ASCII order.
	. Print out the top 5 characters and their counts in the screen. (Your output should be in one line)

Running Examples:
C:\INF1002\Lab2\CountPopularChars>python CountPopularChars.py sdsERwweYxcxeewHJesddsdskjjkjrFGe21DS2145o9003gDDS
d:7,s:7,e:6,j:4,w:3
'''
import sys
from collections import Counter
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def CountPopularChars():
    if len(sys.argv) != 2:
        print("Your input is invalid")
    else:
        try:
            # Convert the string to lowercase and count the frequency of each character
            inputStr = str(sys.argv[1].lower())

            # Get the top 5 most frequent characters and their counts in descending order and ascending ASCII order
            charCount = Counter(inputStr)
		
            #Using sorted(...)[:5] i am chosing from last value (lowest value)
            top5Chars = sorted(charCount.items(), key=lambda item: (-item[1], item[0]))[:5]

            # Convert the list of tuples into a string with the desired format
            strTop5 = ",".join(f"{char}:{count}" for char, count in top5Chars)

            print (strTop5)

        except ValueError:
            print("Your inpout is invalid")
            return

if __name__=='__main__':
          CountPopularChars()
