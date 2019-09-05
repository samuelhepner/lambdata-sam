"""
    Utility functions for working with dataframes
"""
# The imports
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np


class cleanDf:
    # Constructor
    def __init__(self, df):
        self.df = df

    # Finds the nulls and displays how many
    # there are in each column
    def findNull(self, df, col):
        null = df[col].isna().sum()
        return null

    # Helps split your data up and you pick how
    def split(self, df, train_size, test_size):
        train, validate, test = train_test_split(
                                                df, 
                                                train_size=train_size, 
                                                test_size=test_size, 
                                                random_state=42
                                                )
        return train, validate, test
