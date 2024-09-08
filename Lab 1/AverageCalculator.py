'''
Task Description:
Develop a simple average calculator program. The program requirement is as follows:
1. Allow users to run your program with three input arguments by passing three 
   values to the program: a, b and c.

2. Your program will read the three arguments and calculate the average value.

3. After user inputs all the numbers, if the input numbers are invalid, you need to 
   present an error message "Your input is invalid!". Otherwise, you need to print 
   out the average value. The output average value requires to have 2 precisions. 
   For instance, if the value is 23.456, it should print 23.45. If it is 23, 
   it should print 23.00.
   
NOTE: You have to strictly follow the input and output format.

Running example:
Assume your program is named as AverageCalculator.py. Example output is as follows:

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py 3 4 5
Average:4.00

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py 60 39 92
Average:63.67

C:\INF1002\Lab1\AverageCalculator>python AverageCalculator.py abc 10 20
Your input is invalid!
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def AverageCalculator():
   try:
      userInput = input("Enter 3 digits: ")

      # Split the input string into individual components
      value1, value2, value3 = userInput.split()
      value1 = float(value1)
      value2 = float(value2)
      value3 = float(value3)
      
      # Calculate the average
      total = value1 + value2 + value3
      average = total / 3

      print(f"Average: {average:.2f}")
      
   except ValueError:
      print('Your input is invalid!')
      return
   
   pass

             

if __name__=='__main__':
      AverageCalculator()