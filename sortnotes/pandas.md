df = pd.DataFrame(data)
result = df[df['Age'] > 30]
names = df['Name']
selected_columns = df[['Name', 'City']]
sorted_df = df.sort_values(by='Age')
sorted_df = df.sort_values(by=['City', 'Score'], ascending=[True, False])

grouped = df.groupby('City')['Score'].mean()

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Score': [85, 90, 95, 80, 75]
}

df = pd.DataFrame(data)

# Get rows where Age is greater than 30
result = df[df['Age'] > 30]

# Select the 'Name' column
names = df['Name']

# Select 'Name' and 'City' columns
selected_columns = df[['Name', 'City']]

# Group by 'City' and calculate the mean score for each city
grouped = df.groupby('City')['Score'].mean()

# Add a new column 'Passed' based on the 'Score'
df['Passed'] = df['Score'] > 80

# Drop the 'City' column
df = df.drop(columns=['City'])

# Fill missing values in 'Score' column with 0
df['Score'] = df['Score'].fillna(0)

# Drop rows where any value is missing
df = df.dropna()

# Calculate mean age
mean_age = df['Age'].mean()

# Calculate total score
total_score = df['Score'].sum()

# Aggregate 'Score' column with mean and max values
aggregated = df['Score'].agg(['mean', 'max'])

# Merge df1 and df2 on 'ID'
merged = pd.merge(df1, df2, on='ID')

# Apply a lambda function to calculate score percentage
df['Score_Percentage'] = df['Score'].apply(lambda x: x / 100)


df.head()  # Default is 5 rows
df.head(10)  # Displays the first 10 rows
df.tail()  # Default is 5 rows
df.tail(10)  # Displays the last 10 rows

df.info()
Provides a concise summary of the DataFrame, including column names, non-null counts, and data types

df.describe()
Generates summary statistics for numerical columns (like mean, median, standard deviation, etc.).

df.shape
Returns the dimensions of the DataFrame as a tuple (rows, columns)

df.columns
Lists all column names in the DataFrame.

df.dtypes
Displays the data types of each column in the DataFrame.

df.isnull().sum()
Shows the count of missing (null) values in each column.

df.sample()
Returns a random sample of rows from the DataFrame.

df.memory_usage()
Shows the memory usage of each column.

df.nunique()
Returns the number of unique values per column.

df.value_counts()
For a specific column, it returns the counts of unique values.

df.index
Provides information about the index (rows) of the DataFrame.

