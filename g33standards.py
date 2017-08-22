'''
These functions seek to apply the rules
of MSRB g33 to various input types
'''

import decimal

def apply_accrued_interest_rules(num):
    num = decimal.Decimal(str(num)).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
    return str(num)

def apply_dollar_price_rules(num):
    num = decimal.Decimal(str(num)).quantize(decimal.Decimal('.001'), rounding=decimal.ROUND_DOWN)
    return str(num)

def apply_yield_rules(num):
    num = decimal.Decimal(str(num)).quantize(decimal.Decimal('.001'), rounding=decimal.ROUND_HALF_UP)
    return str(num)
