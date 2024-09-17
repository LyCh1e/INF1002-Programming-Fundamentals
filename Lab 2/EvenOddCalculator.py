r'''
Task Description:
In this task, you are assigned to develop one program to help users calculate 
different information based a series of user provided numbers (integers). 
Detailed requirement is provided as follows: 

Input: A series of numbers 
Output: (Your output should be in one line)
       . The summation of the even numbers and summation of the odd numbers in 
       the input list 
	. The difference between the biggest and smallest numbers in the input list
	. The count of even numbers and odd numbers in the input list
	. The "centered" average of the list of integers. The centered average can be 
       calculated as the mean average of the values, after removing the largest and 
       smallest values in the array. If there are multiple copies of the smallest 
       value, ignore all but keep just one copy, and likewise for the largest value. 
       For instance, [12,2,8,7,100] -> 9; [2,2,8,11,100] -> 7

To have a better understanding of the loops, please try to implement 
two programs: one uses "for" and another uses "while" loop.

Running Examples:

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 12,2,8,7,100
The sum of all even numbers is 122, the sum of all odd numbers is 7, 
the difference between the biggest and smallest number is 98, the total number of even numbers is 4, 
the total number of odd numbers is 1, 
the centered average is 9.

C:\INF1002\Lab2\EvenOddCalculator> python EvenOddCalculator.py 1,2,abcd,8,11,200,301
Please enter valid integers.
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def EvenOddCalculator():
    if len(sys.argv) != 2:
        print("Please enter valid integers")
    else:
        try:
            # Convert the input string to a list of integers and calculate the required values
            numbers = [int(num) for num in sys.argv[1].split(",")]
            sumEven = 0
            sumOdd = 0
            
            # maxNumber: initialized to negative infinity (float('-inf')) to ensure any number in the list will be larger.
            # minNumber: Initialized to positive infinity (float('inf')) to ensure any number in the list will be smaller.
            maxNumber = float('-inf')
            minNumber = float('inf')
            countEven = 0
            countOdd = 0
            
            # Calculate the required values using a for loop and update the maximum and minimum numbers as well as 
            # the sum of even and odd numbers and counts of even and odd numbers.
            for num in numbers:
                if num % 2 == 0:
                    sumEven += num
                    countEven += 1
                    maxNumber = max(maxNumber, num) # Updates maxNumber if current number is larger
                    minNumber = min(minNumber, num) # Updates minNumber if current number is smaller
                else:
                    sumOdd += num
                    countOdd += num
					
            centered_average = int((sum(numbers) - maxNumber - minNumber) / (len(numbers) - 2))
            print(f"The sum of all even numbers is {sumEven}, " + 
                f"the sum of all odd numbers is {sumOdd}, " + 
                f"the difference between the biggest and the smallest number is {sumEven}, " + 
                f"the total number of even numbers is {countEven}, " + 
                f"the total number of odd numbers is {countOdd}, " + 
                f"the centered average is {centered_average}")
              
        except ValueError:
            print("Please enter valid integers")

if __name__=='__main__':
      EvenOddCalculator()
      
