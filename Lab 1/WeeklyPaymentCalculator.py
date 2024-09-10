'''
Task Description:
Develop one employee weekly payment calculation program as we have discussed in 
Lecture 2. The program requirement is as follows: 
1.	Allow users to run your program with three input arguments by passing three
    values to the program:  the number of working hours, input normal rate and 
    input the overtime rate.

2.	Your program will read the three arguments and calculate the users salary 
    using the following two formulas:
        a.	Payment of the normal hours = normal rate * normal hours
        b.	Payment of the overtime hours = overtime rate * overtime hours
        NOTE: the working hours within 40 belong to normal hours and those beyond 
              40 hours are considered as overtime hours. 

3.	After user inputs all the numbers, if the input numbers are invalid, you need 
    to present an error message "Your input is invalid!". Otherwise, you need to 
    print out the employee's payment of normal hours, his payment of overtime 
    hours and total payment. The output payment requires to have 2 precisions. 
    For instance, if payment is 2300.456, it should print 2300.45. 
    If payment is 2300, it should print 2300.00.
      
NOTE: You have to strictly follow the input and output format. 

Running example:
Assume your program is named as WeeklyPaymentCalculator.py. Example output is as follows: 

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 20 30 100
Normal Salary:600.00, Extra Salary:0.00, Total Salary:600.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 60 30 200
Normal Salary:1200.00, Extra Salary:4000.00, Total Salary:5200.00

C:\INF1002\Lab1\WeeklyPaymentCalculator> python weeklyPaymentCalculator.py 10000 10 200
Your input is invalid!
'''
import sys
# write your code here
def PayCalaculation(hours, rate):
    pay = rate * hours
    return pay

def WeeklyPaymentCalculator():
    try:
        totalWorkingHrs = float(sys.argv[1])
        normalRate = float(sys.argv[2])
        overtimeRate = float(sys.argv[3])

        # Convert totalWorkingHrs to a float value
        totalWorkingHrs = float(totalWorkingHrs)

        # Check the range of totalWorkingHrs
        if totalWorkingHrs <= 40:
            normalHrs = totalWorkingHrs
            overtimeHrs = 0
        elif totalWorkingHrs > 40 and totalWorkingHrs < 100:
            overtimeHrs = totalWorkingHrs - 40
            normalHrs = 40
        else:
            print("Your input is invalid!")
            return 0

        normalPay = PayCalaculation(normalHrs, float(normalRate))
        overtimePay = PayCalaculation(overtimeHrs, float(overtimeRate))
        totalPay = normalPay + overtimePay

        print(f"Normal Salary:{normalPay:.2f}, Extra Salary:{overtimePay:.2f}, Total Salary:{totalPay:.2f}")
        
    except ValueError:
        print("Your input is invalid!")


if __name__=='__main__':
    if len(sys.argv) != 4:
        print("Your input is invalid!")
    else:
        WeeklyPaymentCalculator()
