'''
Author: Ben Alcoe
Function: This programme tests a compound interest calulator
'''
# initial file testing:
# print('Hello world')
# print('Benjamin Franklin was born in {1600 + 106} in Boston, British America')

from calc import monthly_compounding

def test_tautology():
    assert 3 == 2 + 1
  
# establish input values
def test_zeros_in_zeros_out():
    initial = 0
    monthly = 0 
    annual_rate = 0
    years = 0
    # calculate output
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    #test output via an assertion
    assert final_sum == 0
    
# test with cash inputs

def test_cash():
    initial = 1000
    monthly = 100 
    annual_rate = 0
    years = 1
    # calculate output
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    #test output via an assertion
    assert final_sum == 2200
    
def test_interest_rate():
    initial = 1000
    monthly = 100 
    annual_rate = 12
    years = 1/12
    # calculate output
    final_sum = monthly_compounding(initial, monthly, annual_rate, years)
    #test output via an assertion
    assert final_sum == 1110
    