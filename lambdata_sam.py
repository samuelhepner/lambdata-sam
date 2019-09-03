"""
    Utility functions for working with dataframes
"""
# The imports
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

# Building a dictionary to then become a dataframe
sales = {'Account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
         'Jan': [150, 200, 30],
         'Feb': [210, 300, 12],
         'Mar': [50, 50, 10]}\

# A dataframe built from the dictionary above
df = pd.DataFrame.from_dict(sales)


class cleanDf:
    # Finds the nulls and displays how many
    # there are in each column
    def findNull(df):
        null = df.isna().sum()
        print(null)

    # Helps split your data up and you pick how
    def split(df, train_size, test_size):
        train, validate, test = train_test_split(
                                                df, 
                                                train_size=train_size, 
                                                test_size=test_size, 
                                                random_state=42
                                                )
        return train, validate, test
