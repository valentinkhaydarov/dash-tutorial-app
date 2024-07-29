import pandas as pd

def get_population_data()->pd.DataFrame:
    return pd.read_csv('data/gapminder_unfiltered.csv')