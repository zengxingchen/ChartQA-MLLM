
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 
                'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi Arabia', 'Turkey', 'Switzerland'],
    'Mental Health Budget (% GDP)': [2.8, 1.5, 2.1, 1.8, 0.5, 1.2,
                                     1.5, 0.8, 1.0, 1.3, 0.9, 1.6, 
                                     1.0, 1.4, 0.3, 0.2, 1.5, 0.6, 
                                     0.7, 2.2],
    'Number of Mental Health Professionals (per Million)': [1500, 800, 1200, 1100, 300, 1000,
                                                            900, 400, 600, 1100, 700, 1400, 
                                                            600, 1200, 200, 100, 1300, 400, 
                                                            500, 1600],
    'Population (Millions)': [331, 1438, 126, 83, 1367, 66,
                              65, 213, 60, 38, 145, 51,
                              47, 25, 128, 273, 17,
                              34, 84, 8]
}

df = pd.DataFrame(data)

# Plotting the bubble chart
plt.figure(figsize=(16, 12))
bubble_chart = sns.scatterplot(data=df,
                               x='Mental Health Budget (% GDP)',
                               y='Number of Mental Health Professionals (per Million)',
                               size='Population (Millions)',
                               hue='Mental Health Budget (% GDP)',
                               palette=['#FF6347', '#4682B4', '#8A2BE2', '#3CB371', '#FF4500'],
                               sizes=(100, 2000),
                               alpha=0.7)

plt.title('Mental Health and Well-being by Country', fontsize=20, pad=20)
plt.xlabel('Mental Health Budget (% GDP)', fontsize=14)
plt.ylabel('Number of Mental Health Professionals (per Million)', fontsize=14)
plt.legend(loc='lower right', title='Population (Millions)')

# Show the final plot
plt.show()