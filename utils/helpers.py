


def lower_case_column_names(df):
    """Convert the column names of the dataframe to lower case characters.
    
    Params:
    -------
        df(Pandas DataFrame): The dataframe to be processed.
        
    Return:
    -------
        df(Pandas DataFrame): The dataframe with column names in lower case characters.
    """
    
    col_names = df.columns.values.tolist()
    lower_col_names = [col.lower() for col in col_names]
    df.columns = lower_col_names
    return df

