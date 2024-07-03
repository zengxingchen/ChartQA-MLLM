
import matplotlib.pyplot as plt
import pandas as pd

# Data preparation
data = {
    'Institution': ['Bank A', 'Bank A', 'Bank A', 'Bank A', 'Bank A',
                    'Bank B', 'Bank B', 'Bank B', 'Bank B', 'Bank B',
                    'Bank C', 'Bank C', 'Bank C', 'Bank C', 'Bank C',
                    'Bank D', 'Bank D', 'Bank D', 'Bank D', 'Bank D',
                    'Bank E', 'Bank E', 'Bank E', 'Bank E', 'Bank E'],
    'Year': [2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022,
             2018, 2019, 2020, 2021, 2022],
    'Market Share': [25, 20, 22, 18, 20,
                     15, 18, 20, 22, 25,
                     10, 12, 15, 18, 20,
                     30, 28, 25, 22, 20,
                     20, 22, 18, 20, 15]
}

df = pd.DataFrame(data)

# Pivot the data
pivot_df = df.pivot(index='Year', columns='Institution', values='Market Share')

# Plotting
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFA533']
pivot_df.plot(kind='bar', stacked=True, color=colors, width=0.8, figsize=(10, 6))

# Customization
plt.title('Market Share of Financial Institutions (2018-2022)')
plt.xlabel('Year')
plt.ylabel('Market Share (%)')
plt.legend(title='Institution', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the plot as an image file
plt.savefig('market_share_stacked_bar.png')

# Show the plot
plt.show()