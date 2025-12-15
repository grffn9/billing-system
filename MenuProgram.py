# -------------------------------------------------------------
# Authors: Griffin Munhall, Nicole Isman, Athmika Sreenivas
# Program: MenuProgram
#
# Description:
# Provides the menu to run program4 and program5
# -------------------------------------------------------------
import program4
import program5

def displayMenu():
    print("\nBilling System Menu:")
    print("0 - End")
    print("1 - Enter billing data")
    print("2 - Display ad-hoc billing report")

def main():
    option = None

    while option != "0":
        displayMenu()

        option = input("\nOption ==> ").strip()

        if option == "1":
            program4.writeBillingInformation() 
        elif option == "2":
            program5.adHocReport()
        elif option != "0":
            print("\nPlease enter an available option.")

if __name__ == "__main__":
    main()
