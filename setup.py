import pandas as pd
import pytest

def test_duplicates():
  print("Coming Here")
  df = pd.read_csv("abc.csv")
  for column in df.columns:
    assert any(df.duplicated(subset=[column])) 

    
if __name__ == '__main__':
    test_duplicates()
