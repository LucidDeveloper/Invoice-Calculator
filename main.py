# Developer: Gianni M. Javier
# Created: 02/03/2024
# Last Update: 03/14/2025

# This program calculates the daily gross pay, taxes, net pay, and service charge for a pay period. 
# It then writes each days pay and the total to a file.

# Enter py (or python) main.py into the terminal from the working directory 
# where the program is located in order to run the program.

# Functions
from functions.calculate_invoice import calculate_invoice
from functions.calculate_total import calculate_total
from functions.create_file import create_file
from functions.write_invoice import write_invoice
from functions.write_total import write_total


# Main
def main():
    
    # Variables
    day = 0
    hourly_rate = 19.15
    tax_rate = 0.26
    total_hours = 0.00
    total_gross_pay = 0.00
    total_taxes = 0.00
    total_net_pay = 0.00
    total_service_charge = 0.00

    print("\nWhat was the start date for this pay period? (MMDDYYYY)")
    input_start_date = input()
    month_start = input_start_date[0:2]
    day_start = input_start_date[2:4]
    year_start = input_start_date[4:8]
    input_start_date = month_start + "_" + day_start + "_" + year_start

    print("What was the end date for this pay period? (MMDDYYYY)")
    input_end_date = input()
    month_end = input_end_date[0:2]
    day_end = input_end_date[2:4]
    year_end = input_end_date[4:8]
    input_end_date = month_end + "_" + day_end + "_" + year_end

    directory = "C:/Users/Gianni/Desktop/Software Engineering/Projects/InvoiceCalculator/archive/"
    file_name = "_pay_period_" + input_start_date + "_to_" + input_end_date
    file = year_end + file_name + ".txt"
    file_path = directory + file

    file_exists = create_file(file_path, file)

    if file_exists == True:
        print("\n(Continuing will OverWrite file.)")
        print("(Enter 0 to Read file to Console and Exit\nEnter 1 to OverWrite file.)")
        continue_input = input()
        continue_input = int(continue_input)
        
        if continue_input == 0:
            file = open(file_path, 'r')
            print(file.read())
            file.close()
            exit()
        else:
            print("\nHow many days did you work during this pay period? (dd)")
    else:
        print("\nHow many days did you work during this pay period? (dd)")
        
    input_days = input()
    days = int(input_days)

    if days < 1:
        file = open(file_path, 'r')
        print(file.read())
        file.close()
        exit()
        
    while day < days:
        print(f"\nEnter the date for workday {day + 1}: (MMDDYYYY)")
        input_date = input()
        
        if len(input_date) != 8:
            print("Invalid date format. Please enter a valid date.")
            continue
        
        date = input_date[0:2] + "/" + input_date[2:4] + "/" + input_date[4:8]
        
        print(f"Enter the number of hours worked on workday {day + 1}: (hh.mm)")
        input_hours = input()
        
        if input_hours == "":
            print("Invalid hours format. Please enter a valid number of hours.")
            continue

        hours = float(input_hours)

        gross_pay, taxes, net_pay, service_charge = calculate_invoice(hours, hourly_rate, tax_rate)
        write_invoice(file_path, file_name, date, hours, day, hourly_rate, gross_pay, taxes, net_pay, service_charge)
        total_hours, total_gross_pay, total_taxes, total_net_pay, total_service_charge = calculate_total(hours, gross_pay, taxes, net_pay, service_charge, total_hours, total_gross_pay, total_taxes, total_net_pay, total_service_charge)
        day += 1

    write_total(file_path, file_name, total_hours, total_gross_pay, total_taxes, total_net_pay, total_service_charge)

    file = open(file_path, 'r')
    print(file.read())
    file.close()

if __name__ == "__main__":
    main()