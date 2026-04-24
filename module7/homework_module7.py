def clean_department(df):
    """Normalize the department column to Title Case and drop rows where department is null.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with a 'department' column.

    Returns
    -------
    pd.DataFrame
        DataFrame with department column normalized and no null department values.
    """
    df = df.copy()
    df = df.dropna(subset=["department"])
    df["department"] = df["department"].str.lower().str.title()
    return df
