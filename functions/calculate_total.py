# Developer: Gianni M. Javier
# Created: 02/03/2024
# Last Update: 01/31/2025

# Function
# calculate totals
def calculate_total(hours, gross_pay, taxes, net_pay, service_charge, total_hours, total_gross_pay, total_taxes, total_net_pay, total_service_charge):
    total_hours += hours
    total_gross_pay += gross_pay
    total_taxes += taxes
    total_net_pay += net_pay
    total_service_charge += service_charge
    return total_hours, total_gross_pay, total_taxes, total_net_pay, total_service_charge