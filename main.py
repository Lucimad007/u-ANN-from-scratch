import pandas as pd

# Load the datasets
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

# Check the first few rows of the datasets
print(train_df.head())
print(test_df.head())
