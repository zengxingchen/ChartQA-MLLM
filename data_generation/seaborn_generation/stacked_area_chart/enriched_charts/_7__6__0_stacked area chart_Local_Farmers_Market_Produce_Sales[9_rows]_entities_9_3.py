
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing the data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022', 'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'Communication Satellites': [10, 12, 15, 18, 20, 22, 25, 28, 30, 33, 35, 38],
    'Earth Observation Satellites': [5, 6, 8, 9, 10, 12, 14, 16, 18, 20, 22, 25],
    'Scientific Satellites': [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

# Calculate the cumulative launches
cumulative_launches = df.cumsum(axis=1)

# Set the plot size
plt.figure(figsize=(16, 10))

# Plotting the data
plt.stackplot(df.index, cumulative_launches['Communication Satellites'],
              cumulative_launches['Earth Observation Satellites'],
              cumulative_launches['Scientific Satellites'],
              labels=['Communication Satellites', 'Earth Observation Satellites', 'Scientific Satellites'],
              colors=['#FF6347', '#4682B4', '#8A2BE2'], alpha=0.8)

# Adding the legend
plt.legend(loc='upper left')

# Annotating a specific point
plt.annotate('Most Launches', xy=('Q4-2023', cumulative_launches.loc['Q4-2023', 'Scientific Satellites']),
             xytext=(-80, 30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

# Adding title and labels
plt.title('Quarterly Satellite Launches by Type', pad=40)
plt.xlabel('Quarter')
plt.ylabel('Number of Launches')

# Display the plot
plt.tight_layout()
plt.show()