import pandas as pd

def explore_metadata():
    # Load the metadata.csv file
    df = pd.read_csv('metadata.csv', low_memory=False)
    
    # Print the shape of the DataFrame
    print(f"DataFrame shape: {df.shape}")
    
    # Print the first 5 rows
    print("First 5 rows:")
    print(df.head())
    
    # Print data types of each column
    print("\\nData types:")
    print(df.dtypes)
    
    # Print count of missing values per column
    print("\\nMissing values per column:")
    print(df.isnull().sum())

if __name__ == "__main__":
    explore_metadata()
