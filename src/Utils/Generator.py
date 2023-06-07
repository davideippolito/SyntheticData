# --------------------------------------------------------------------------- #
#                                   IMPORT                                    #
# --------------------------------------------------------------------------- #

import pandas as pd

from faker import Faker
import random

from sdv.metadata import SingleTableMetadata
from sdv.metadata import MultiTableMetadata


# --------------------------------------------------------------------------- #
#                                  VARIABLES                                  #
# --------------------------------------------------------------------------- #

regions = [
        'Abruzzo', 'Basilicata', 'Calabria', 'Campania', 'Emilia-Romagna',
        'Friuli-Venezia Giulia', 'Lazio', 'Liguria', 'Lombardia', 'Marche',
        'Molise', 'Piemonte', 'Puglia', 'Sardegna', 'Sicilia', 'Toscana',
        'Trentino-Alto Adige', 'Umbria', 'Valle d\'Aosta', 'Veneto'
    ]

account_types = ['Conto Corrente', 'Conto Deposito']

employment_types = ['Tempo Pieno', 'Tempo Parziale', 'Libero Professionista']

loan_terms = ['None', '12 months', '24 months', '36 months', '60 months', '120 months']


# --------------------------------------------------------------------------- #
#                                   DATASETS                                  #
# --------------------------------------------------------------------------- #

def generate_banking_dataset(n):
    fake = Faker('it_IT')
    dataset = []

    for _ in range(n):
        data = {
            'Customer_ID': fake.random_number(digits=21),
            'Account_Number': fake.random_number(digits=10),
            'Account_Type': random.choice(account_types),
            'Balance': round(random.uniform(0, 1000000), 2),
            # ! Negative values implications on Correlation multipliers:
            # 'Balance': round(random.uniform(-10000, 1000000), 2), 
            'Currency': 'EUR',
            'Last_Transaction Date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            'Last_Transaction Amount': round(random.uniform(-10000, 10000), 2),
            'Tot_Transaction_Amount': round(random.uniform(0, 100000), 2),
            'Branch': fake.city(),
            'Region': random.choice(regions),
            'Address': fake.address().replace('\n', ', '),
            'Phone': '+0039' + str(fake.random_number(digits=9)),
            'Email': fake.email(),
            'Employer': fake.company(),
            'Employment_Type': random.choice(employment_types),
            'Credit_Score': random.randint(300, 850),
            'Loan_Amount': round(random.uniform(1000, 100000), 2),
            'Loan_Term': random.choice(loan_terms),
            'Interest_Rate': round(random.uniform(1, 15), 2)
        }
        dataset.append(data)

    return dataset

# --------------------------------------------------------------------------- #

def generate_financial_dataset(n):
    fake = Faker()
    dataset = []

    for _ in range(n):
        data = {
            'Account_Number': fake.random_number(digits=10),
            'Account_Type': random.choice(['Checking', 'Savings']),
            'Balance': round(random.uniform(0, 1000000), 2),
            'Currency': random.choice(['USD', 'EUR', 'GBP']),
            'Transaction_Date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            'Transaction_Amount': round(random.uniform(-10000, 10000), 2),
            'Category': random.choice(['Investments', 'Mortgages', 'Insurance', 'Loans', 'Retirement']),
            'Description': fake.catch_phrase(),
            'Customer_Name': fake.name(),
            'Address': fake.address().replace('\n', ', '),
            'City': fake.city(),
            'Country': fake.country(),
            'Phone': fake.phone_number(),
            'Email': fake.email(),
            'Employer': fake.company(),
            'Employment_Type': random.choice(['Full-time', 'Part-time', 'Self-employed']),
            'Credit_Score': random.randint(300, 850),
            'Loan_Amount': round(random.uniform(1000, 100000), 2),
            'Loan_Term': random.choice(['12 months', '24 months', '36 months']),
            'Interest_Rate': round(random.uniform(1, 15), 2)
        }
        dataset.append(data)

    return dataset


# --------------------------------------------------------------------------- #
#                                   METADATA                                  #
# --------------------------------------------------------------------------- #

def generate_metadata_st(data):
    # Generate metadata from input
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data)

    # Correct metadata sd types
    metadata.update_column(
        column_name='Customer_ID',
        sdtype='id',
        regex_format=r'\d{21}'
    )

    # Primary Keys: These keys identify every row of the table. 
    # They must be unique to the entire table and other tables may refer to them.
    metadata.set_primary_key(
        column_name='Customer_ID'
    )

    # Return metadata
    return metadata

# --------------------------------------------------------------------------- #

def generate_metadata_mt(data):
    # Add the DataFrame to the dictionary
    datasets = {}
    datasets['d1'] = data

    # Generate metadata from input
    metadata = MultiTableMetadata()
    metadata.detect_table_from_dataframe(
        table_name='d1',
        data=data
    )

    # Correct metadata sd types
    metadata.update_column(
        table_name='d1',
        column_name='Customer_ID',
        sdtype='id',
        regex_format=r'\d{21}'
    )

    # Primary Keys: These keys identify every row of the table. 
    # They must be unique to the entire table and other tables may refer to them.
    metadata.set_primary_key(
        table_name='d1',
        column_name='Customer_ID'
    )

    # Return metadata
    return metadata

# --------------------------------------------------------------------------- #