r'''
Task Description:
In this task, you will develop a program to compute all the leap years within a 
specified time period. The user will input a start year and an end year. 
Your task is to determine how many leap years are included in this period and 
print out those leap years. 

The rule for determining leap years is as follows:
	. A year is called a leap year, if the year is perfectly divisible by 4 - except 
       for years which are both divisible by 100 and not divisible by 400. The second 
       part of the rule effects century years. 
       For example; the century years 1600 and 2000 are leap years, 
       but the century years 1700, 1800, and 1900 are not. This means that three times 
       out of every 400 years there are 8 years between leap years.

More information about the leap years rule can be found online. 

Input: Two numbers (one is the start year, and another is the end year)
Output: The number of leap years and all the leap years (Your output should be in one line)
Note: In case of invalid input, print the message "Your input is invalid!".

Running Examples:

C:\INF1002\Lab2\LeapYearCalculator> python LeapYearCalculator.py 1989 2000
The number of Leap Years is 3, the Leap Years are 1992, 1996, 2000
'''

import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.
def LeapYearCalculator():
    if len(sys.argv) != 3:
        print("Your input is invalid!")
          
    else:
        try:
            startYear = int(sys.argv[1])
            endYear = int(sys.argv[2])
               
            if startYear > endYear:
                print("Your input is invalid!")
                return
               
            leapYears = []
            for year in range(startYear, endYear + 1):

                # Checks if the year is divisible by 4, which is a requirement for a year to be a leap year.
                if year % 4 == 0:
                    
                    # Checks if the year not divisible by 100 and divisible by 400, 
                    # which is a condition for a year to be a leap year.
                    if year % 100 != 0 or year % 400 == 0:
                        leapYears.append(year)
                              
            print(f"The number of Leap Years is {len(leapYears)}, the Leap Years are {', '.join(map(str, leapYears))}")

        except ValueError:
            print("Your input is invalid!")

if __name__=='__main__':
     LeapYearCalculator()
      
