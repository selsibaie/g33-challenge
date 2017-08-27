'''
summary
'''


#standard import
import sys
import g33standards

inputtype = input("Please enter a letter indicating if the user will input Accrued Interest, Dollar Price, or Yield (i.e., “A”, “D”, or “Y”): ")
num = input("Please enter a number: ")

if inputtype == "A":
    print(g33standards.apply_accrued_interest_rules(num))
elif inputtype == "D":
    print(g33standards.apply_dollar_price_rules(num))
elif inputtype == "Y":
    print(g33standards.apply_yield_rules(num))
else:
    pass