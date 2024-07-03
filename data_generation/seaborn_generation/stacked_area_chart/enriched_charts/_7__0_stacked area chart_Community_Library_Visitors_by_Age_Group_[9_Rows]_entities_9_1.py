
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Data
data = {
    'Year': [i for i in range(2000, 2021)],
    'Cardio': [3100 + i * 50 for i in range(21)],
    'Yoga': [1600 + i * 10 for i in range(21)],
    'Strength': [2100 + i * 25 for i in range(21)],
    'HIIT': [600 + i * 10 for i in range(21)],
    'Cycling': [330 + i * 3 for i in range(21)],
}
df = pd.DataFrame(data)

# Melting the data to long format
df_melted = df.melt('Year', var_name='Exercise', value_name='Participants')

# Pivot for cumulative sum to stack the sectors on top of each other
df_melted['Cumulative'] = df_melted.groupby('Year')['Participants'].cumsum()

# Plot
plt.figure(figsize=(14, 8))
colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A8", "#33FFF2"]

# Loop to create the stacked area plot
for i, exercise in enumerate(df_melted['Exercise'].unique()):
    if i == 0:
        plt.fill_between(df['Year'], 0, df_melted[df_melted['Exercise'] == exercise]['Cumulative'], color=colors[i], label=exercise)
    else:
        plt.fill_between(df['Year'], 
                         df_melted[df_melted['Exercise'] == df_melted['Exercise'].unique()[i-1]]['Cumulative'], 
                         df_melted[df_melted['Exercise'] == exercise]['Cumulative'], 
                         color=colors[i], label=exercise)

# Annotating the last value of Cardio for example
last_year_data = df_melted[df_melted['Year'] == df['Year'].max()]
cardio_last_value = last_year_data[last_year_data['Exercise'] == 'Cardio']['Cumulative'].values[0]
plt.text(df['Year'].max(), cardio_last_value - 250, "Cardio", verticalalignment='center', horizontalalignment='center', color="white", fontsize=10)

# Customizing the plot
plt.title("Fitness Participants Over Time by Exercise Type", pad=20)
plt.xlabel("Year")
plt.ylabel("Number of Participants (Thousands)")
plt.legend(loc='upper right')
sns.despine()
plt.show()