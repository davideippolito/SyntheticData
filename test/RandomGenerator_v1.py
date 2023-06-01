import random
from faker import Faker

def datasetGenerator(n):
    fake = Faker()
    data = []
    
    for _ in range(n):
        entry = {
            'NDG': str(fake.random_number(digits=21)),
            'Segment': str(fake.random_int(min=1, max=4) * 10),
            'Region': random.choice(['Lombardia', 'Lombardia', 'Lombardia', 'Trentino', 'Veneto', 'Veneto', 'Toscana', 'Sicilia']),
            'Age Range': random.choice(['25', '35', '45', '45', '55', '55', '65', '65', '65']),
            'Gender': random.choice(['F', 'M']),
            'Income': float(fake.random_int(min=1000, max=100000)),
            'Duration': str(fake.random_int(min=1, max=35))
        }
        data.append(entry)
    
    return data
