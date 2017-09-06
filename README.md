# g33-challenge

## Summary

This program will prompt the user for two inputs:
- A letter indicating if the user will input Accrued Interest, Dollar Price, or Yield (i.e., “A”, “D”, or “Y”)
- A number

Upon entering the two inputs, the program will perform a rounding function consistent with the "Standards of Accuracy; Truncation rounding rules of MSRB Rule G-33" (below)

The user can continue entering numbers repeatedly, but has a way to exit when boredom threshold is exceeded

#### Rule G-33

Standards of Accuracy; Truncation.

(i) Intermediate Values. All values used in computations of accrued interest, yield, and dollar price shall be computed to not less than ten decimal places.

(ii) Results of Computations. Results of computations shall be presented in accordance with the following:

(A) Accrued interest shall be truncated to three decimal places, and rounded to two decimal places immediately prior to presentation of total accrued interest amount on the confirmation;

(B) Dollar prices shall be truncated to three decimal places immediately prior to presentation of dollar price on the confirmation and computation of extended principal; and

(C) Yields shall be truncated to four decimal places, and rounded to three decimal places, provided, however, that for purposes of confirmation display as required under rule G-15(a) yields accurate to the nearest .05 percentage points shall be deemed satisfactory.

Numbers shall be rounded, where required, in the following manner: if the last digit after truncation is five or above, the preceding digit shall be increased to the next highest number, and the last digit shall be discarded.

## How to use
Execute "run.py" using the python 3.6 interpreter, and interactively supply the information the application requests.

## How to run tests
Install pytest: `pip install -U pytest`

Run pytest through interpreter: `python -m pytest unittest.py`

Further documentation: https://docs.pytest.org/en/latest/contents.html

## Dependencies
Python 3.6