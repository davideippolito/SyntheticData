def correlation_income_age_range(data):
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

def correlation_income_region(data):
    for _ in data:
        if _['Region'] == 'Lombardia':
            _['Income'] = _['Income'] * 2.5
        elif _['Region'] in ['Toscana', 'Trentino']:
            _['Income'] = _['Income'] * 1.5
        elif _['Region'] in ['Sicilia', 'Veneto']:
            _['Income'] = _['Income'] * 1