import g33standards

def test_accrued_interest():
    assert g33standards.apply_accrued_interest_rules(4.1269834) == "4.13"
    assert g33standards.apply_accrued_interest_rules(4.124) == "4.12"
    assert g33standards.apply_accrued_interest_rules(4.1249834) == "4.12"
    assert g33standards.apply_accrued_interest_rules(21.1246956908732) == "21.12"
    assert g33standards.apply_accrued_interest_rules(29384.2445089) == "29384.24"
    assert g33standards.apply_accrued_interest_rules(2.035) == "2.04"
    assert g33standards.apply_accrued_interest_rules(2.045) == "2.05"
    assert g33standards.apply_accrued_interest_rules(-2.045) == "-2.05"
    assert g33standards.apply_accrued_interest_rules(-2.035) == "-2.04"

def test_dollar_price():
    assert g33standards.apply_dollar_price_rules(4.1269834) == "4.126"
    assert g33standards.apply_dollar_price_rules(-2.1535) == "-2.153"
    assert g33standards.apply_dollar_price_rules(-2.1534) == "-2.153"

def test_yield():
    assert g33standards.apply_yield_rules(4.1269834) == "4.127"
    assert g33standards.apply_yield_rules(-2.1535) == "-2.154"
    assert g33standards.apply_yield_rules(-2.1534) == "-2.153"
