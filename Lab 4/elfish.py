r'''
Task Description: 
     A word is considered elfish if it contains the letters: e, l and f in it, in any 
     order. For instance, we would say that the following words are elfish: tasteful, 
     whiteleaf, unfriendly and waffles, because they each contain those letters. Use 
     the recursive function to implement this. Write one program to call your recursive 
     function and tell the user whether the input word is one elfish or not. 
     
     HINT: You can recursively reduce both the elfish letters and input word. 
     The sample executions are provided as follows:

Note: 
     Your output should be in ONE line

Running example: 
     C:\INF1002\Lab4\elfish> python elfish.py waffles
     waffles is one elfish word!

     C:\INF1002\Lab4\elfish> python elfish.py instance
     instance is not an elfish word!
'''

import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def elfish_recursive(word, letters = "elf"):
    if len(letters) == 0:
        return True  # All elfish letters found
    if len(word) == 0:
        return False # No more letters in the word, but elfish letters remain

    # Check if the first letter of the word is in the elfish letters, if so, remove it from letters
    if word[0] in letters:
        # Recursively check the remaining letters in the word and the updated elfish letters
        return elfish_recursive(word[1:], letters.replace(word[0], '', 1))
    else:
        # If the first letter of the word is not in the elfish letters, check the remaining letters in the word
        return elfish_recursive(word[1:], letters)

def elfish():
    if len(sys.argv) != 2:
        print("Your input is invalid.")
        return
    else:
        try:
            word = str(sys.argv[1].lower())

            if elfish_recursive(word) == True:
                print(f"{word} is one elfish word!")
            else:
                print(f"{word} is not an elfish word!")
                
        except ValueError:
            print("Your input is invalid.")
            return
          
if __name__=='__main__':
    elfish()
      
