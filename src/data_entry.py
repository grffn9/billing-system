# -------------------------------------------------------------
# Authors: Griffin Munhall, Nicole Isman, Athmika Sreenivas
# Program: Program4
#
# Description:
# Calculates the total hours worked, average hours worked per week, 
# and the total amount due to the employee at the end of the month, 
# given a set of inputs (accounts for bonus hours beyond 160/month),
# writes the employee information to "Billing.txt", and finally, 
# asks if you'd like to enter another employee
# -------------------------------------------------------------
import BillingModule

def writeBillingInformation():
    BillingModule.resetBillingFile()

    totalHours = 0.0
    averageHours = 0.0
    overtimeHours = 0.0
    invoiceAmount = 0.0
    additionalPay = 0.0
    overtimeRate = 0.0
    continueProgram = "y"
    overtimeAmountMessage = ""
    overtimePayMessage = ""
    regularHoursMessage = ""
    WEEKS_IN_MONTH = 4
    REGULAR_MONTHLY_HOURS = 160
    OVERTIME_RATE_INCREASE = 0.05
    
    while continueProgram == "y":
        employeeName = BillingModule.readEmployeeName("\nEmployee Name: ")
        hourlyRate = BillingModule.readHourlyRate("Hourly Rate: ")
        week1Hours = BillingModule.readWeeklyHours("Enter hours worked for week 1: ")
        week2Hours = BillingModule.readWeeklyHours("Enter hours worked for week 2: ")
        week3Hours = BillingModule.readWeeklyHours("Enter hours worked for week 3: ")
        week4Hours = BillingModule.readWeeklyHours("Enter hours worked for week 4: ")

        totalHours = week1Hours + week2Hours + week3Hours + week4Hours
        averageHours = totalHours / WEEKS_IN_MONTH

        if totalHours > REGULAR_MONTHLY_HOURS:
            overtimeHours = totalHours - REGULAR_MONTHLY_HOURS
            overtimeRate = round(hourlyRate + hourlyRate * OVERTIME_RATE_INCREASE, 2)
            additionalPay = round(overtimeRate * overtimeHours, 2)
            invoiceAmount = (REGULAR_MONTHLY_HOURS * hourlyRate) + additionalPay
            overtimeAmountMessage = f"\n{employeeName} worked {overtimeHours:.1f} hours of overtime.\n"
            overtimePayMessage = f"Overtime Hours: {overtimeHours:.2f} @ ${overtimeRate:,.2f}\t= ${additionalPay:,.2f}\n"
            regularHoursMessage = f"Regular Hours: {REGULAR_MONTHLY_HOURS:.2f} @ ${hourlyRate:,.2f}\t= ${REGULAR_MONTHLY_HOURS * hourlyRate:,.2f}"
        else:
            invoiceAmount = totalHours * hourlyRate
            overtimeAmountMessage = f"\n{employeeName} worked no overtime.\n"
            overtimePayMessage = ""
            regularHoursMessage = f"Regular Hours: {totalHours:.2f} @ ${hourlyRate:,.2f}\t= ${invoiceAmount:,.2f}"

        print(overtimeAmountMessage)
        print("Invoice")
        print(f"Resource: {employeeName}\tAverage weekly hours: {averageHours:,.2f}\n")
        print(f"Total billable hours: {totalHours:.2f}\trate: ${hourlyRate:,.2f}")
        print(overtimePayMessage, end="")
        print(regularHoursMessage)
        print(f"Amount Due: ${invoiceAmount:,.2f}")

        BillingModule.writeBillingRecord(employeeName, hourlyRate, week1Hours, week2Hours, week3Hours, week4Hours)

        continueProgram = input('\nEnter another employee? ("y"=yes"): ')
        
def main():
    writeBillingInformation()

if __name__ == "__main__":
    main()
