# Calculate income tax for the given income by following the below rules

"""
Taxable Income	                      Rate (in %)
First  $10,000	                      0
Next   $10,000	                      10
The remaining                           20

"""

def taxes_income(income):
    if income <= 10000:
        tax = 0
        income_with_taxes = income * (1-(tax/100))
    elif income > 10000 and income <= 20000:
        tax = 10
        income_with_taxes = income * (1-(tax/100))
    else:
        tax = 20
        income_with_taxes = income * (1-(tax/100))
        
    
    print(f"Your income without the taxes is ${income:.2f}, the tax for your income is {tax}% and your income with the deducted taxes is ${income_with_taxes:.2f} ")

taxes_income(1000)
taxes_income(10000)
taxes_income(10001)
taxes_income(20000)
taxes_income(20001)



'''Muslim Solution:
income = 30000
tax_payable = 0

print("Given Income:", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    tax_payable = (income - 10000) * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100

    tax_payable += (income - 20000) * 20 / 100

print("Total payable tax amount is", tax_payable)
'''