# --------------------------------------------------------------------------- #
#                                  FUNCTIONS                                  #
# --------------------------------------------------------------------------- #

def dependency_balance_employment_type(data):
    for _ in data:
        if _['Employment_Type'] == 'Tempo Pieno':
            _['Balance'] *= 1
        elif _['Employment_Type'] == 'Tempo Parziale':
            _['Balance'] *= 0.5
        elif _['Employment_Type'] == 'Libero Professionista':
            _['Balance'] *= 1.5

def dependency_balance_region(data):
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
            _['Credit_Score'] *= 2
        elif 10000 <= _['Tot_Transaction_Amount'] <= 50000:
            _['Credit_Score'] *= 1
        elif _['Tot_Transaction_Amount'] <= 10000:
            _['Credit_Score'] *= 0.2
            
# --------------------------------------------------------------------------- #
