import unittest
from lambdata_sam import *


class lambdata_sam_test(unittest.TestCase):
    def test_clean(self):
        clean_df = cleanDf(df=df)
        self.assertEqual(clean_df.findNull(df=df, col='Jan'), 0)

if __name__ == '__main__':
    # Building a dictionary to then become a dataframe
    sales = {'Account': ['Jones LLC', 'Alpha Co', 'Blue Inc'],
             'Jan': [150, 200, 30],
             'Feb': [210, 300, 12],
             'Mar': [50, 50, 10]}\

    # A dataframe built from the dictionary above
    df = pd.DataFrame.from_dict(sales)
    unittest.main()
    