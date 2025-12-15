# -------------------------------------------------------------
# Authors: Griffin Munhall, Nicole Isman, Athmika Sreenivas
# Program: Program5
#
# Description:
# Provides the ad-hoc management report
# -------------------------------------------------------------


def adHocReport(fileName="Billing.txt"):
    try:
        with open(fileName, "r") as file:
            totalBillableDue = 0.0
            totalBillingHours = 0.0
            employeeCount = 0
            REGULAR_MONTHLY_HOURS = 160
            OVERTIME_RATE_INCREASE = 1.05
            NUMBER_OF_WEEKS_WORKED = 4
            MINIMUM_EMPLOYEE_COUNT = 0

            header = f"\n{'Employee':<15}{'Rate':<10}{'week 1':<8}{'week 2':<8}{'week 3':<8}{'week 4':<8}{'Hours':<8}{'Total':<10}\n"
            report = ""

            line = file.readline().strip()

            while line != "":
                employeeName = line

                hourlyRate = float(file.readline().strip())
                week1Hours = float(file.readline().strip())
                week2Hours = float(file.readline().strip())
                week3Hours = float(file.readline().strip())
                week4Hours = float(file.readline().strip())

                totalHours = week1Hours + week2Hours + week3Hours + week4Hours

                if totalHours > REGULAR_MONTHLY_HOURS:
                    overtimeHours = totalHours - REGULAR_MONTHLY_HOURS
                    overtimeRate = round(hourlyRate * (OVERTIME_RATE_INCREASE), 2)
                    overtimePay = round(overtimeHours * overtimeRate, 2)
                    regularPay = round(REGULAR_MONTHLY_HOURS * hourlyRate, 2)
                    invoiceAmount = regularPay + overtimePay
                else:
                    invoiceAmount = round(totalHours * hourlyRate, 2)

                totalBillingHours += totalHours
                totalBillableDue += invoiceAmount
                employeeCount += 1

                report += (
                    f"{employeeName:<15}${hourlyRate:<9.2f}"
                    f"{week1Hours:<8.2f}{week2Hours:<8.2f}{week3Hours:<8.2f}{week4Hours:<8.2f}"
                    f"{totalHours:<8.2f}${invoiceAmount:,.2f}\n"
                )

                line = file.readline().strip()

            if employeeCount >= MINIMUM_EMPLOYEE_COUNT:
                averageBillableHours = totalBillingHours / (employeeCount * NUMBER_OF_WEEKS_WORKED)
                summary = (
                    f"\nTotal Billable Due:\t${totalBillableDue:,.2f}\n"
                    f"Total Billable Hours:\t{totalBillingHours:.2f}\n"
                    f"Average Billable Hours:\t{averageBillableHours:.2f}"
                )
            else:
                summary = "\nNo employees on file.\n"

    except FileNotFoundError:
        header = ""
        report = ""
        summary = f"\nError: The file '{fileName}' does not exist. Please run the Billing Entry program first."
    except ZeroDivisionError:
        header = f"\n{'Employee':<15}{'Rate':<10}{'week 1':<8}{'week 2':<8}{'week 3':<8}{'week 4':<8}{'Hours':<8}{'Total':<10}\n"
        report = ""
        summary = "No employees on file."

    print(header + report + summary)


def main():
    adHocReport()


if __name__ == "__main__":
    main()
