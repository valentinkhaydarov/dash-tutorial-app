import pandas as pd

def get_population_data()->pd.DataFrame:
    # Provides the raw dataset
    return pd.read_csv('data/gapminder_unfiltered.csv')