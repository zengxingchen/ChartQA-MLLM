
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Region': ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia', 'Middle East', 'Central America', 'Caribbean'],
    'AwarenessCampaigns': [150, 180, 300, 80, 60, 50, 40, 30, 20],
    'Population': [579.3, 746.4, 4636.6, 430.8, 1340.6, 25.5, 411.0, 182.8, 44.5],
    'Funding': [1200.5, 1350.3, 950.2, 500.1, 200.4, 300.6, 250.2, 150.7, 100.3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(18, 10))
bubble = sns.scatterplot(data=df, x='AwarenessCampaigns', y='Population', size='Funding', hue='Region', 
                         palette=['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1', 
                                  '#FF9DA7', '#9C755F'], 
                         sizes=(100, 2000), alpha=0.8, edgecolor='black')

plt.title('Mental Health Awareness by Region in 2023', fontsize=20, pad=20)
plt.xlabel('Number of Awareness Campaigns', fontsize=14)
plt.ylabel('Population (Millions)', fontsize=14)

# Customize legend
hand, labl = bubble.get_legend_handles_labels()
bubble.legend(hand[1:], labl[1:], title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()