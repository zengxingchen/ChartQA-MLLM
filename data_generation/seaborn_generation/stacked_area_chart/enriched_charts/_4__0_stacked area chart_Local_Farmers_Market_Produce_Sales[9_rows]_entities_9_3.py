
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing the data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Rock': [60.25, 65.47, 67.89, 70.55, 73.12, 75.45, 78.98, 80.45, 82.12, 85.56, 88.12, 90.56],
    'Pop': [70.33, 72.15, 75.88, 78.23, 80.56, 83.12, 85.44, 88.12, 90.45, 92.78, 95.23, 98.12],
    'HipHop': [55.78, 60.22, 62.34, 65.98, 68.45, 70.23, 73.89, 76.33, 78.67, 80.99, 83.45, 86.78]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

# Calculate the cumulative revenue
cumulative_revenue = df.cumsum(axis=1)

# Set the plot size
plt.figure(figsize=(14, 8))

# Plotting the data
plt.stackplot(df.index, cumulative_revenue['Rock'],
              cumulative_revenue['Pop'],
              cumulative_revenue['HipHop'],
              labels=['Rock', 'Pop', 'HipHop'],
              colors=['#1f77b4', '#ff7f0e', '#2ca02c'], alpha=0.8)

# Adding the legend
plt.legend(loc='upper left')

# Annotating a specific point
plt.annotate('Highest Pop Genre', xy=('Q4-2023', cumulative_revenue.loc['Q4-2023', 'Pop']),
             xytext=(-100, 20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

# Adding title and labels
plt.title('Music Genres Quarterly Revenue (in millions)', fontsize=14)
plt.xlabel('Quarter')
plt.ylabel('Revenue')

# Display the plot
plt.tight_layout()
plt.show()