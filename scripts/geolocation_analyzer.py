import pandas as pd
import geopandas as gpd
import plotly.express as px

class GeolocationAnalyzer:
    def __init__(self, fraud_data_path: str, world_data_path: str):
        """
        Initializes the GeolocationAnalysis class with paths to the fraud and world data.

        Args:
            fraud_data_path (str): Path to the CSV file containing fraud transaction data.
            world_data_path (str): Path to the shapefile containing world geometries.
        """
        self.fraud_data_path = fraud_data_path
        self.world_data_path = world_data_path
        self.fraud_df = pd.read_csv(fraud_data_path)  # Load fraud data
        self.world = gpd.read_file(world_data_path)    # Load world geometries
        self.fraud_rate_df = None                       # DataFrame for fraud rates
        self.transaction_volume_df = None               # DataFrame for transaction volumes

    def calculate_fraud_rate(self):
        """
        Calculates the fraud rate by country and stores it in the fraud_rate_df attribute.
        The fraud rate is computed as the number of fraudulent transactions divided by the total transactions for each country.
        """
        total_by_country = self.fraud_df['country'].value_counts()
        fraud_by_country = self.fraud_df[self.fraud_df['class'] == 1]['country'].value_counts()

        # Create a DataFrame for fraud rates
        self.fraud_rate_df = pd.DataFrame({
            'country': total_by_country.index,
            'fraud_rate': (fraud_by_country / total_by_country).fillna(0).values
        }).reset_index(drop=True)
        
        return self.fraud_rate_df

    def calculate_transaction_volume(self):
        """
        Calculates the total transaction volume by country and stores it in the transaction_volume_df attribute.
        """
        transaction_volume_by_country = self.fraud_df['country'].value_counts().reset_index()
        transaction_volume_by_country.columns = ['country', 'transaction_volume']
        self.transaction_volume_df = transaction_volume_by_country
        
        return self.transaction_volume_df

    def merge_data(self):
        """
        Merges the fraud rates and transaction volumes with the world GeoDataFrame.
        Updates the world_fraud_map attribute with the merged data.
        Missing values are filled with zeros.
        """
        # Merge fraud rates and transaction volumes with the world GeoDataFrame
        self.world_fraud_map = self.world.merge(self.fraud_rate_df, how='left', left_on='NAME', right_on='country')
        self.world_fraud_map = self.world_fraud_map.merge(self.transaction_volume_df, how='left', left_on='country', right_on='country')
        
        # Fill missing values with 0
        self.world_fraud_map['fraud_rate'] = self.world_fraud_map['fraud_rate'].fillna(0)
        self.world_fraud_map['transaction_volume'] = self.world_fraud_map['transaction_volume'].fillna(0)

    def plot_fraud_rate_map(self):
        """
        Creates and displays an interactive map of fraud rates by country using Plotly.
        """
        fig = px.choropleth(
            self.world_fraud_map,
            geojson=self.world_fraud_map.geometry,
            locations=self.world_fraud_map.index,
            color='fraud_rate',
            hover_name='NAME',
            hover_data=['fraud_rate', 'transaction_volume'],
            title='Interactive Fraud Rate by Country',
            color_continuous_scale='Reds',
            projection='natural earth',
        )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.show()

    def plot_transaction_volume_map(self):
        """
        Creates and displays an interactive map of transaction volumes by country using Plotly.
        """
        fig = px.choropleth(
            self.world_fraud_map,
            geojson=self.world_fraud_map.geometry,
            locations=self.world_fraud_map.index,
            color='transaction_volume',
            hover_name='NAME',
            hover_data=['transaction_volume', 'fraud_rate'],
            title='Interactive Transaction Volume by Country',
            color_continuous_scale='Blues',
            projection='natural earth',
        )
        fig.update_geos(fitbounds="locations", visible=False)
        fig.show()

    def analyze(self):
        """
        Executes the full geolocation analysis, including calculating fraud rates, transaction volumes,
        merging the data, and plotting the results.
        """
        self.calculate_fraud_rate()
        self.calculate_transaction_volume()
        self.merge_data()
        self.plot_fraud_rate_map()
        self.plot_transaction_volume_map()
