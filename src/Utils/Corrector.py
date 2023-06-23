# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

import random
from faker import Faker

# --------------------------------------------------------------------------- #
#                                  VARIABLES                                  #
# --------------------------------------------------------------------------- #

fake = Faker()

# --------------------------------------------------------------------------- #
#                                  FUNCTIONS                                  #
# --------------------------------------------------------------------------- #

def correct_age_range_duration(data):
    for _ in data:
        age_range = int(_['Age Range'])
        duration = int(_['Duration'])
        if age_range - duration < 18:
            _['Duration'] = str(fake.random_int(min=1, max=7))

def correct_tot_transaction_amount(data):
    for _ in data:
        if _['Tot_Transaction_Amount'] < _['Last_Transaction_Amount']:
            _['Tot_Transaction_Amount'] += _['Last_Transaction_Amount']

# --------------------------------------------------------------------------- #
