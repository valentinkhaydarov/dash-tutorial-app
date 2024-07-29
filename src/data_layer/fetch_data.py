import pandas as pd

def get_population_data()->pd.DataFrame:
    """Provides the raw dataset

    Returns:
        pd.DataFrame: Population data from different countries
    """
    return pd.read_csv('data/gapminder_unfiltered.csv')