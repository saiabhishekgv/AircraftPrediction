import pandas as pd
import pytest

def test_duplicates():
  df = pd.read_csv("abc.csv")
  for column in df.columns:
    assert df.column.is_unique

    
if __name__ == '__main__':
    test_duplicates()


