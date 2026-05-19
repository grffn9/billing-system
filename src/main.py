# -------------------------------------------------------------
# Authors: Griffin Munhall, Nicole Isman, Athmika Sreenivas
# Program: MenuProgram
#
# Description:
# Provides the menu to run program4 and program5
# -------------------------------------------------------------
import data_entry
import report
import utils

def displayMenu():
    print("\nBilling System Menu:")
    print("0 - End")
    print("1 - Enter billing data")
    print("2 - Display ad-hoc billing report")
    print("3 - Reset billing data")

def main():
    option = None

    while option != "0":
        displayMenu()

        option = input("\nOption ==> ").strip()

        if option == "1":
            data_entry.writeBillingInformation() 
        elif option == "2":
            report.adHocReport()
        elif option == "3":
            utils.resetBillingFile()
            print("\nBilling data reset successfully.")
        elif option != "0":
            print("\nPlease enter an available option.")

if __name__ == "__main__":
    main()
