import pandas as pd

from src.data_layer.fetch_data import get_population_data

def get_country_list() -> pd.DataFrame:
    # Provides a list of countries available in the dataset
    data = get_population_data()
    return data['country'].unique()

def prepare_plot_data(country: str) -> pd.DataFrame:
    # Provides data with population changes for the plot
    data = get_population_data()
    country_data = data[data['country']==country]
    plot_data = country_data.copy()
    plot_data['pop_diff'] = country_data['pop'].diff()
    return plot_data