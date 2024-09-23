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
    else:
        try:
            # Convert the first argument (candidate sequence) to a list of integers.
            candidate = list(map(int, sys.argv[1].split(',')))
            # Convert the second argument (pattern) to a list of integers.
            pattern = list(map(int, sys.argv[2].split(',')))

            patternFound = 0
            
            # Iterate through the candidate sequence, checking for the pattern, +1 is to make sure it iterates the full list 
            for i in range(len(candidate) - len(pattern) + 1):
                # Check if the subsequence of candidate starting at index i and of length len(pattern) matches the pattern.
                if candidate[i:i+len(pattern)] == pattern:
                    patternFound += 1

            print(f"Pattern appears {patternFound} time!")

        except ValueError:
            print("Your input is invalid.")
            return

if __name__=='__main__':
     SearchPattern()
      
