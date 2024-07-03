
import pandas as pd
import matplotlib.pyplot as plt

# Preparing the data
data = {
    'Quarter': ['Q1-2021', 'Q2-2021', 'Q3-2021', 'Q4-2021', 'Q1-2022', 'Q2-2022', 'Q3-2022', 'Q4-2022',
                'Q1-2023', 'Q2-2023', 'Q3-2023', 'Q4-2023'],
    'RealEstate': [120.15, 130.22, 140.45, 150.32, 160.75, 170.20, 180.45, 190.90, 200.15, 210.65, 220.90, 230.45],
    'Technology': [110.25, 115.75, 120.85, 125.50, 130.35, 135.80, 140.95, 146.50, 152.25, 157.75, 163.35, 169.05],
    'Healthcare': [100.10, 105.35, 110.65, 115.95, 121.05, 126.45, 132.10, 137.60, 143.20, 148.85, 154.65, 160.25]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

# Calculate the cumulative revenue
cumulative_revenue = df.cumsum(axis=1)

# Set the plot size
plt.figure(figsize=(16, 10))

# Plotting the data
plt.stackplot(df.index, cumulative_revenue['RealEstate'],
              cumulative_revenue['Technology'],
              cumulative_revenue['Healthcare'],
              labels=['Real Estate', 'Technology', 'Healthcare'],
              colors=['#004c6d', '#ff6f61', '#2a9d8f'], alpha=0.85)

# Adding the legend
plt.legend(loc='upper left')

# Annotating a specific point
plt.annotate('Highest Tech Investment', xy=('Q4-2023', cumulative_revenue.loc['Q4-2023', 'Technology']),
             xytext=(-100, 30), textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

# Adding title and labels
plt.title('Quarterly Revenue in Different Investment Sectors (in millions)', fontsize=16)
plt.xlabel('Quarter')
plt.ylabel('Revenue')

# Display the plot
plt.tight_layout()
plt.show()