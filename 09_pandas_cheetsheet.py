import pandas as pd
# -----------------------------------------------------------
# 1. Specify values for each column
df = pd.DataFrame({'a': [4, 5, 6],
                   'b': [7, 8, 9],
                   'c': [10, 11, 12]}, index = [1, 2, 3])

# -----------------------------------------------------------
# 2. Specify values for each row
df2 = pd.DataFrame([[4, 7, 10],
                    [5, 8, 11],
                    [6, 9, 12]],
                   index = [1, 2, 3], columns=['a', 'b', 'c'])

# -----------------------------------------------------------
# 3. Create DataFrame with a MultiIndex
df3 = pd.DataFrame({'a': [4, 5, 6],
                    'b': [7, 8, 9],
                    'c': [10, 11, 12]},
                   index=pd.MultiIndex.from_tuples([('d', 1), ('d', 2), ('e', 2)], names=['n', 'v']))

# -----------------------------------------------------------
# 4. Reshaping Data - Change the layout of a data set
# Gater columns into rows
pd.melt(df)

# Append columns of DataFrame
# pd.concat([df1, df2], axis=1)

# Order rows by values of a column (high to row)
# df.sort_values('mpg', ascending=False)

# Rename the columns of a DataFrame
df.rename(columns={'y':'year'})

# Sort the index of a DataFrame
df.sort_index()

# Reset index of DataFrame to row numbers, moving index to columns
df.reset_index()

# -----------------------------------------------------------
# 5. Subset Observations
# Extract rows that meet logical criteria
df[df.Length > 7]

# Remove duplicate rows (only considers columns)
df.drop_duplicates()

# Select first n rows
df.head(n)

# Select last n rows
df.tail(n)

# Randomly select fraction of rows
df.sample(frac=0.5)

# Randomly select in rows
df.sampel(n=10)

# Select rows by position
df.iloc[10:20]

# Select and order top n entries
df.nlargest(n, 'value')

# Select and order bottom n entries
df.nsmallest(n, 'value')

# -----------------------------------------------------------
# 6. Subset Variables
# Select multiple columns with specific names
df[['width', 'length', 'species']]

# Select single column with specific name
df['width'] or df.width

# Select columns whose name matches regular expression regex
df.filter(regex='regex')