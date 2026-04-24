# Copy this to test_homework_module7.py and run with: pytest test_homework_module7.py -v

import pandas as pd
from homework_module7 import clean_department

def test_clean_department_returns_dataframe():
    df_input = pd.DataFrame({"department": ["engineering", "HR"]})
    result = clean_department(df_input)
    assert isinstance(result, pd.DataFrame)

def test_clean_department_normalizes_case():
    df_input = pd.DataFrame({"department": ["engineering", "MARKETING", "HR"]})
    result = clean_department(df_input)
    expected = ["Engineering", "Marketing", "Hr"]
    assert result["department"].tolist() == expected

def test_clean_department_removes_nulls():
    df_input = pd.DataFrame({"department": ["Engineering", None, "HR"]})
    result = clean_department(df_input)
    assert result["department"].notna().all()
    assert len(result) == 2