# Developer: Gianni M. Javier
# Created: 02/03/2024
# Last Update: 05/01/2025

# Function
# calculate invoice
def calculate_invoice(hours, hourly_rate, tax_rate):
    gross_pay = hours * hourly_rate
    taxes = gross_pay * tax_rate
    net_pay = gross_pay - taxes
    service_charge = gross_pay * 0.30  # Assuming a fixed service fee of 30% the gross income
    return gross_pay, taxes, net_pay, service_charge
