# Developer: Gianni M. Javier
# Created: 02/03/2024
# Last Updated: 03/14/2025

# write totals to file
def write_total(file_path, file_name, total_hours, total_gross_pay, total_taxes, total_net_pay, total_service_charge):
    file = open(file_path, "a")
    file.write(file_name + "\n")
    file.write("====================================\n")
    file.write("Invoice Totals\n")
    file.write(f"Total Hours: {total_hours:.2f}\n")
    file.write(f"Total Gross Pay: ${total_gross_pay:.2f} (before taxes)\n")
    file.write(f"Total Taxes (25%): ${total_taxes:.2f}\n")
    file.write(f"Total Net Pay: ${total_net_pay:.2f} (after taxes)\n")
    file.write(f"Total Service Charge: ${total_service_charge:.2f}\n")
    file.write(f"Final Pay: ${(total_net_pay - total_service_charge):.2f} (after taxes and service charge)\n")
    file.write("\n")
    file.close()
    return