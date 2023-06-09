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

loan_terms = ['12 months', '24 months', '36 months', '60 months', '120 months']


# --------------------------------------------------------------------------- #
#                                   DATASET                                   #
# --------------------------------------------------------------------------- #

def generate_banking_dataset(n):
    fake = Faker('it_IT')
    dataset = []
    for _ in range(n):
        data = {
            'Customer_ID': fake.random_number(digits=21),
            'SSN': str(fake.ssn()),
            'Account_Number': fake.random_number(digits=10),
            'Account_Type': str(random.choice(account_types)),
            'Balance': round(random.uniform(0, 1000000), 2),
            'Currency': 'EUR',
            'Last_Transaction_Date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d'),
            'Last_Transaction_Amount': round(random.uniform(-10000, 10000), 2),
            'Tot_Transaction_Amount': round(random.uniform(0, 100000), 2),
            'Branch': str(fake.city()), # implicit type for metadata
            'Region': str(random.choice(regions)),
            'Address': str(fake.address().replace('\n', ', ')),
            'Email': str(fake.email()),
            'Phone': '+0039 ' + str(fake.random_number(digits=9)),
            'Company': str(fake.company()), # implicit type for metadata
            'Employment_Type': str(random.choice(employment_types)),
            'Credit_Score': random.randint(300, 850),
            'Loan_Amount': round(random.uniform(1000, 100000), 2),
            'Loan_Term': str(random.choice(loan_terms)),
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
    # Add the DataFrame to the dictionary
    metadata.detect_table_from_dataframe(
        data=data
    )
    # Correct id type
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
    metadata.add_alternate_keys(
        column_names=['Account_Number']
    )
    metadata.add_alternate_keys(
        column_names=['SSN']
    )
    # Personal Identifiable Information (PII)
    metadata.update_column(
        column_name='Address',
        sdtype='address',
        pii=True
    )
    metadata.update_column(
        column_name='Email',
        sdtype='email',
        pii=True
    )
    metadata.update_column(
        column_name='Phone',
        sdtype='phone_number',
        pii=True
    )
    # Correct metadata sd types
    metadata.update_column(
        column_name='Last_Transaction_Date',
        sdtype='datetime',
        datetime_format='%Y-%m-%d'
    )
    metadata.update_column(
        column_name='Region',
        sdtype='categorical'
    )
    metadata.update_column(
        column_name='Account_Type',
        sdtype='categorical'
    )
    metadata.update_column(
        column_name='Employment_Type',
        sdtype='categorical'
    )
    metadata.update_column(
        column_name='Loan_Term',
        sdtype='categorical'
    )
    # Return metadata
    return metadata

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
    # Correct id type
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
    metadata.add_alternate_keys(
        table_name='d1',
        column_names=['Account_Number']
    )
    metadata.add_alternate_keys(
        table_name='d1',
        column_names=['SSN']
    )
    # Personal Identifiable Information (PII)
    metadata.update_column(
        table_name='d1',
        column_name='Address',
        sdtype='address',
        pii=True
    )
    metadata.update_column(
        table_name='d1',
        column_name='Email',
        sdtype='email',
        pii=True
    )
    metadata.update_column(
        table_name='d1',
        column_name='Phone',
        sdtype='phone_number',
        pii=True
    )
    # Correct metadata sd types
    metadata.update_column(
        table_name='d1',
        column_name='Last_Transaction_Date',
        sdtype='datetime',
        datetime_format='%Y-%m-%d'
    )
    metadata.update_column(
        table_name='d1',
        column_name='Region',
        sdtype='categorical'
    )
    metadata.update_column(
        table_name='d1',
        column_name='Account_Type',
        sdtype='categorical'
    )
    metadata.update_column(
        table_name='d1',
        column_name='Employment_Type',
        sdtype='categorical'
    )
    metadata.update_column(
        table_name='d1',
        column_name='Loan_Term',
        sdtype='categorical'
    )
    # Return metadata
    return metadata

# --------------------------------------------------------------------------- #
