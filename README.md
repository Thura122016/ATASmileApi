# ATASmileApi

To connect Smile One Api

step 0 -> You should have Merchant account for Smile One.<br>
step 1 -> Fill blanks in the ATAConfig_.py<br>
step 2 -> Rename ATAConfig_.py to ATAConfig.py<br>
step 3 -> That's all.<br>

## Offline tests

Run `python -B -m unittest discover -s tests -v` from the repository directory.
The tests use Python's standard library, the blank configuration template, and a
mock HTTP client. They do not read `ATAConfig.py`, require merchant credentials,
send network requests, or place orders. Installing `requests` is not necessary
to run these tests.

Verified with Python 3.13.14. These tests check the wrapper's request routing and
do not establish live merchant API or storefront compatibility.
