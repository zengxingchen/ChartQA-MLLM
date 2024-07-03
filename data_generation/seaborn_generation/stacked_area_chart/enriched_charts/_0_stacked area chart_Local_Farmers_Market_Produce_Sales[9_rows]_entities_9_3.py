
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Preparing the data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022'],
    'Apple': [89.58, 81.43, 83.36, 123.95, 97.28, 83.36, 90.15, 120.47],
    'Google': [55.31, 61.88, 65.12, 75.33, 68.01, 70.26, 65.11, 81.44],
    'Amazon': [108.52, 113.08, 110.81, 125.56, 108.52, 115.06, 111.55, 137.41]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

# Calculate the cumulative revenue
cumulative_revenue = df.cumsum(axis=1)

# Set the plot size
plt.figure(figsize=(12, 6))

# Plotting the data
plt.stackplot(df.index, cumulative_revenue['Apple'],
              cumulative_revenue['Google'],
              cumulative_revenue['Amazon'],
              labels=['Apple', 'Google', 'Amazon'],
              colors=['#FF9500', '#4285F4', '#FF9900'], alpha=0.8)

# Adding the legend
plt.legend(loc='upper left')

# Annotating a specific point
plt.annotate('Highest Revenue', xy=('Q4-2022', cumulative_revenue.loc['Q4-2022', 'Amazon']),
             xytext=(20, -20), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

# Adding title and labels
plt.title('Tech Companies Quarterly Revenue (in billions)')
plt.xlabel('Quarter')
plt.ylabel('Revenue')

# Display the plot
plt.tight_layout()
plt.show()