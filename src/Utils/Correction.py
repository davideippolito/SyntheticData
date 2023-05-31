from faker import Faker
import random

fake = Faker()

def correct_age_range_duration(data):
    for _ in data:
        age_range = int(_['Age Range'])
        duration = int(_['Duration'])
        if age_range - duration < 18:
            _['Duration'] = str(fake.random_int(min=1, max=7))