'''
These functions seek to apply the rules
of MSRB g33 to various input types
'''

import decimal

def apply_accrued_interest_rules(num):
    c = decimal.Decimal(num).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
    return str(c)
