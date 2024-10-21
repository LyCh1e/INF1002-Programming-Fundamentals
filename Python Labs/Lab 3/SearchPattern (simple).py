r'''
Task Description:
     In this task you will write a program that reads two sequences of numbers. 
     The first sequence of numbers is called candidate, and the second sequence of 
     numbers is called pa􀆩ern. Your program will determine if the pa􀆩ern is found 
     entirely in the candidate. To be considered found entirely, all elements of 
     pattern must be in the candidate sequence a consecu􀆟ve positions. You must 
     output the number of found patterns, or 0 if the pattern is not found in 
     the candidate.

     Input: 
          Allow the users to input two sequences, the first sequence is the candidate, 
          and the second sequence is the pattern.
     Output: 
          The number of pattern sequence appearing in the candidate sequence (in ONE line).

     Running Example:
     C:\INF1002\Lab3\PatternSearching>python SearchPattern.py 1,2,3,1,2 1,2
     Pattern appears 2 time!
'''

import sys

def SearchPattern():
    if len(sys.argv) != 3:
        print("Your input is invalid.")
        return
    else:
        try:
            # Convert input strings to lists of integers and join them into a single string
            candidateList = sys.argv[1].split(',')
            candidate = str(''.join(map(str, candidateList)))

            # Convert input strings to lists of integers and join them into a single string
            patternlist = sys.argv[2].split(',')
            pattern = str(''.join(map(str, patternlist)))

            # Check if the pattern is found in the candidate and print the count of occurrences if found
            if pattern in candidate:
                print(f"Pattern appears {candidate.count(pattern)} time!")

        except:
            print("Your input is invalid")

if __name__=='__main__':
     SearchPattern()
      