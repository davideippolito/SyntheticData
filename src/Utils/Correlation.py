# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

import random


# --------------------------------------------------------------------------- #
#                                  FUNCTIONS                                  #
# --------------------------------------------------------------------------- #

def dependency_balance_employment_type(data):
    for _ in data:
        if _['Employment_Type'] == 'Tempo Pieno':
            _['Balance'] *= 1
        elif _['Employment_Type'] == 'Tempo Parziale':
            _['Balance'] *= 0.8
        elif _['Employment_Type'] == 'Libero Professionista':
            _['Balance'] *= 1.5
        # elif _['Employment_Type'] == 'Libero Professionista':
        #     _['Balance'] *= random.choice([0.2, 0.5, 1.5, 2, 2.5, 10])

def dependency_region_balance(data):
    for _ in data:
        if _['Region'] == 'Lombardia':
            _['Balance'] *= 2
        elif _['Region'] in ['Friuli-Venezia Giulia', 'Trentino', 'Piemonte', 'Trentino-Alto Adige', 'Valle d\'Aosta', 'Veneto']:
            _['Balance'] *= 1.5
        elif _['Region'] in ['Abruzzo', 'Emilia-Romagna', 'Lazio', 'Marche', 'Molise', 'Toscana']:
            _['Balance'] *= 1
        elif _['Region'] in ['Basilicata', 'Calabria', 'Campania', 'Puglia', 'Sicilia']:
            _['Balance'] *= 0.5
        elif _['Region'] in ['Sardegna', 'Sicilia']:
            _['Balance'] *= 0.1

def dependency_tot_transaction_amount_credit_score(data):
    for _ in data:
        if _['Tot_Transaction_Amount'] >= 50000:
            _['Credit_Score'] *= 1.2
        elif 10000 <= _['Tot_Transaction_Amount'] <= 50000:
            _['Credit_Score'] *= 1
        elif _['Tot_Transaction_Amount'] <= 10000:
            _['Credit_Score'] *= 0.8


# --------------------------------------------------------------------------- #
#                                    OLDER                                    #
# --------------------------------------------------------------------------- #

def dependency_income_age_range(data):
    for _ in data:
        if _['Age Range'] == '65':
            _['Income'] = _['Income'] * 2
        elif _['Age Range'] == '55':
            _['Income'] = _['Income'] * 2.5
        elif _['Age Range'] == '45':
            _['Income'] = _['Income'] * 1.5
        elif _['Age Range'] == '35':
            _['Income'] = _['Income'] * 1
        elif _['Age Range'] == '25':
            _['Income'] = _['Income'] * 0.5