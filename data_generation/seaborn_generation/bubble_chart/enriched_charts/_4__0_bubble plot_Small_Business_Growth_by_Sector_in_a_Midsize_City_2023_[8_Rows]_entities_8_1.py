
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 
                'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi Arabia', 'Turkey', 'Switzerland'],
    'Participation Rate (%)': [60, 45, 70, 65, 30, 62,
                               68, 50, 55, 72, 40, 75, 
                               67, 78, 35, 28, 69, 25, 
                               33, 80],
    'Average Weekly Exercise Hours': [5, 4, 6, 6.5, 3.5, 5.5,
                                      6, 4.5, 5, 7, 3.5, 6.5, 
                                      6, 7.5, 4, 3, 6.5, 2.5, 
                                      3.5, 7.5],
    'Population (Millions)': [331, 1438, 126, 83, 1367, 66,
                              65, 213, 60, 38, 145, 51,
                              47, 25, 128, 273, 17,
                              34, 84, 8]
}

df = pd.DataFrame(data)

# Plotting the bubble chart
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df,
                               x='Participation Rate (%)',
                               y='Average Weekly Exercise Hours',
                               size='Population (Millions)',
                               hue='Participation Rate (%)',
                               palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
                               sizes=(20, 800),
                               alpha=0.7)

plt.title('Sports & Fitness Indicators of Different Countries', fontsize=16)
plt.xlabel('Participation Rate (%)', fontsize=14)
plt.ylabel('Average Weekly Exercise Hours', fontsize=14)
plt.legend(loc='upper right', title='Population (Millions)')

# Show the final plot
plt.show()