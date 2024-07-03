
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'France', 'Brazil', 'Canada', 'Russia', 'Australia', 'Japan', 'UK', 'South Korea', 'Italy', 'Spain', 'Others'],
    'CO2Emissions': [5000, 10000, 2500, 2000, 1500, 1000, 1200, 3500, 900, 1800, 1400, 1300, 1000, 900, 5000],
    'RenewableEnergyProduction': [300, 500, 350, 450, 400, 600, 550, 200, 500, 300, 450, 250, 400, 350, 2000],
    'Investment': [800, 1200, 600, 700, 650, 400, 500, 550, 450, 800, 600, 500, 450, 420, 1000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(18, 14))
bubble = sns.scatterplot(data=df, x='RenewableEnergyProduction', y='CO2Emissions', size='Investment', hue='Country', 
                         palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#57FFC1', '#FFD133', '#8333FF', 
                                  '#33FFF7', '#FF335B', '#FF9733', '#7333FF', '#33FF97', '#737373', '#FF57A6', '#57FF33'], 
                         sizes=(50, 1500), alpha=0.7, edgecolor='black')

plt.title('CO2 Emissions and Renewable Energy Production by Country in 2023', fontsize=20)
plt.xlabel('Renewable Energy Production (GWh)', fontsize=14)
plt.ylabel('CO2 Emissions (MtCO2)', fontsize=14)

# Customize legend
hand, labl = bubble.get_legend_handles_labels()
bubble.legend(hand[1:], labl[1:], title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()