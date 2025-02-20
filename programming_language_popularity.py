import pandas as pd
import matplotlib.pyplot as plt

"""** Reading the csv file **"""
# Changing the header with our own names: DATE, TAG, and POSTS
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

df.head()
df.tail()
df.shape
df.count()

df['POSTS']
df['POSTS'].count()
df.groupby('TAG').sum()
df.groupby('TAG').count()

"""** Changing datetime type **"""
# Changing the datetime from str to datetime type, which is better for numeric date-time value
df.DATE = pd.to_datetime(df.DATE)

# Pivoting the dataframe to reshape it
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.head()
reshaped_df.count()

"""** Data Cleaning: Replacing NaN values with 0 **"""
reshaped_df.fillna(0, inplace=True)

reshaped_df.isna().values.any()

""" ** Data Manipulation **"""
# The technique that helps us to organize the data, showing the relationship between different tags and posts
# In this case, the Date is in the rows, and the number of posts for each programming language (TAG) is the columns.
reshaped_df.head()

# Save the reshaped dataframe to a new CSV file
reshaped_df.to_csv('reshaped_data.csv')

"""** Plotting the reshaped data **"""
plt.figure(figsize=(16, 10))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# Plotting the data for each column (programming language) in reshaped_df
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], label=column)

plt.legend(fontsize=16)

"""** Smoothing Out Time Series Data **"""
# Using rolling mean to smooth out the noisy time series data
roll_df = reshaped_df.rolling(window=6).mean()

# Save the rolling mean dataframe to a new CSV file
roll_df.to_csv('rolling_data.csv')

"""** Plotting the Rolling Mean Data **"""
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# Plot the rolling mean data for each tag
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
plt.show()
