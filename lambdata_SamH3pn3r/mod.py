"""
    A simple python lambdata
"""

import pandas as pd
from sklearn.model_selection import train_test_split

sales = {'Account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
        'Jan': [150, 200,30],
        'Feb': [210,300,12],
        'Mar': [50,50,10]}
# for testing
df = pd.DataFrame.from_dict(sales)

def findNull(df):
    null = df.isna().sum()
    print(null)

def split(df, train_size, test_size):
    train, validate, test = train_test_split(df, train_size=train_size, test_size=test_size, random_state=42)
    return train, validate, test
