# -------------------------------------------------------------
# Authors: Griffin Munhall, Nicole Isman, Athmika Sreenivas
# Program: BillingModule
#
# Description:
# Provides the functionality for program 4, gathering the 
# input for weekly hours, hourly rate, employee name, 
# resetting the billing file, and writing a billing record
# -------------------------------------------------------------
import os

def readWeeklyHours(inputPrompt):
    MINIMUM_HOURS_WORKED = 35
    MAXIMUM_HOURS_WORKED = 80
    while True:
        try:
            hoursInput = float(input(inputPrompt))
            if MINIMUM_HOURS_WORKED <= hoursInput <= MAXIMUM_HOURS_WORKED:
                return hoursInput
            else:
                print("Invalid number of hours, must be between 35 and 80.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def readHourlyRate(inputPrompt):
    MINIMUM_HOURLY_RATE = 20.0
    while True:
        try:
            hourlyRate = float(input(inputPrompt))
            if hourlyRate >= MINIMUM_HOURLY_RATE:
                return hourlyRate
            else:
                print("Invalid Hourly Rate, must be at least $20.00/hour.\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

def readEmployeeName(inputPrompt):
    MINIMUM_EMPLOYEE_NAME_LENGTH = 1
    while True:
        employeeName = input(inputPrompt)
        if len(employeeName) >= MINIMUM_EMPLOYEE_NAME_LENGTH:
            return employeeName
        print("Employee name must be entered.")

def resetBillingFile(fileName=None):
    if fileName is None:
        fileName = os.path.join("data", "Billing.txt")
    with open(fileName, "w") as _:
        pass

def writeBillingRecord(employeeName, hourlyRate, week1Hours, week2Hours, week3Hours, week4Hours, fileName=None):
    if fileName is None:
        fileName = os.path.join("data", "Billing.txt")
    with open(fileName, "a") as file:
        file.write(f"{employeeName}\n{hourlyRate}\n{week1Hours}\n{week2Hours}\n{week3Hours}\n{week4Hours}\n")
