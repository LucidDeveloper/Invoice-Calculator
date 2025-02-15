# Developer: Gianni M. Javier
# Created: 02/03/2024
# Last Update: 01/31/2025

# Function
# write invoice to file
def write_invoice(file_path, file_name, date, hours, day, hourly_rate, gross_pay, taxes, net_pay, service_charge):
    if day == 0:
        file = open(file_path, "w")
        file.write("\n" + file_name + "\n")
        file.write("====================================\n")
        file.write(f"Day {day + 1} Invoice\n")
        file.write(f"Date: {date} (Day {day + 1})\n")
        file.write("Hours: " + str(hours) + "\n")
        file.write(f"Hourly Pay Rate: ${hourly_rate:.2f}\n")
        file.write(f"Gross Pay: ${gross_pay:.2f}\n")
        file.write(f"Taxes (25%): ${taxes:.2f}\n")
        file.write(f"Net Pay: ${net_pay:.2f}\n")
        file.write(f"Service Charge (10%): ${service_charge:.2f}\n")
        file.write(f"Final Pay: ${(net_pay - service_charge):.2f}\n")
        file.write("\n")
        file.close()
    else:
        file = open(file_path, "a")
        file.write(f"Day {day + 1} Invoice\n")
        file.write(f"Date: {date} (Day {day + 1})\n")
        file.write("Hours: " + str(hours) + "\n")
        file.write(f"Hourly Pay Rate: ${hourly_rate:.2f}\n")
        file.write(f"Gross Pay: ${gross_pay:.2f}\n")
        file.write(f"Taxes (25%): ${taxes:.2f}\n")
        file.write(f"Net Pay: ${net_pay:.2f}\n")
        file.write(f"Service Charge (10%): ${service_charge:.2f}\n")
        file.write(f"Final Pay: ${(net_pay - service_charge):.2f}\n")
        file.write("\n")
        file.close()
    
    # check output on the terminal
    # print("\nDate: ", input_date)
    # print("Hours: ", input_hours)
    # print("Rate: ", input_rate)
    # print("Gross Pay: ", gross_pay)
    # print("Taxes: ", taxes)
    # print("Net Pay: ", net_pay)
    # print("Service Charge: ", service_charge)
    return