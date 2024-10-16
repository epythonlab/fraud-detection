import pandas as pd
import numpy as np

class DataPreprocessor:
    """
    A class for preprocessing a dataset, including loading, cleaning, and handling missing values.

    Attributes:
    ----------
    filepath : str
        The file path of the dataset.
    logger : logging.Logger
        The logger instance for logging actions and errors.
    data : pd.DataFrame, optional
        The dataset loaded from the file path.
    """

    def __init__(self, filepath, logger):
        """
        Initializes the DataPreprocessor with a dataset filepath and logger.

        Parameters:
        ----------
        filepath : str
            The path to the dataset file (CSV format).
        logger : logging.Logger
            A logger instance for logging information and errors.
        """
        self.filepath = filepath
        self.logger = logger
        self.data = None
    
    def load_dataset(self):
        """
        Loads the dataset from the specified filepath.

        Returns:
        -------
        pd.DataFrame
            The loaded dataset as a DataFrame.
        """
        try:
            self.data = pd.read_csv(self.filepath)
            self.logger.info("Dataset loaded successfully.")
            return self.data
        except Exception as e:
            self.logger.error(f"Error loading dataset: {e}")
            return None  # Return None if there's an error loading the dataset
        

    def handle_missing_values(self, strategy='drop', fill_value=None):
        """
        Handles missing values in the dataset based on the specified strategy.

        Parameters:
        ----------
        strategy : str, optional
            The strategy for handling missing values: 'drop' or 'impute' (default is 'drop').
        fill_value : object, optional
            The value to use for imputation if strategy is 'impute' (default is None).
        """
        if self.data is not None:
            if strategy == 'drop':
                self.data.dropna(inplace=True)
                self.logger.info("Missing values dropped.")
            elif strategy == 'impute' and fill_value is not None:
                self.data.fillna(fill_value, inplace=True)
                self.logger.info(f"Missing values imputed with: {fill_value}")
            else:
                self.logger.error("Invalid strategy or fill value missing for imputation.")
        else:
            self.logger.warning("No dataset loaded. Please load the dataset first.")

    def clean_data(self):
        """
        Cleans the dataset by removing duplicates and correcting data types where necessary.
        """
        if self.data is not None:
            # Remove duplicate rows
            initial_shape = self.data.shape
            self.data.drop_duplicates(inplace=True)
            duplicates_removed = initial_shape[0] - self.data.shape[0]
            self.logger.info(f"Removed {duplicates_removed} duplicate rows.")

            # Attempt to convert object columns to numeric if applicable
            for col in self.data.columns:
                if self.data[col].dtype == 'object':
                    try:
                        self.data[col] = pd.to_numeric(self.data[col], errors='ignore')
                        self.logger.info(f"Converted column '{col}' to numeric if applicable.")
                    except Exception as e:
                        self.logger.error(f"Error converting column '{col}': {e}")

            self.logger.info("Data cleaning complete.")
        else:
            self.logger.warning("No dataset loaded. Please load the dataset first.")
