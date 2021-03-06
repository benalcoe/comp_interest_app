'''
Author: Ben Alcoe
Function: This calculates the compound interest
'''
def monthly_compounding(initial, monthly, annual_rate, years):
    
    final_sum = initial
    
    months = years * 12
    
    for months in range(int(months)):
        final_sum = final_sum * (1 + annual_rate / 1200) + monthly
        
    return final_sum


