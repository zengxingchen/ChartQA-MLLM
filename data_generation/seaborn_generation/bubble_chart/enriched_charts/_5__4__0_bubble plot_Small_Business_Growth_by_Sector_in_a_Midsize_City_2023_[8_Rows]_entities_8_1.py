
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Country': ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom',
                'France', 'Brazil', 'Italy', 'Canada', 'Russia', 'South Korea', 
                'Spain', 'Australia', 'Mexico', 'Indonesia', 'Netherlands', 
                'Saudi Arabia', 'Turkey', 'Switzerland'],
    'Research Budget (% GDP)': [3.5, 2.1, 3.2, 2.9, 0.8, 1.7,
                                2.2, 1.1, 1.4, 1.9, 1.0, 4.3, 
                                1.2, 2.0, 0.4, 0.2, 2.3, 0.9, 
                                0.6, 3.4],
    'Number of Researchers (per Million)': [5000, 1500, 5500, 4000, 1200, 4300,
                                            4500, 900, 3500, 4800, 1300, 6100, 
                                            3000, 3200, 500, 400, 4700, 800, 
                                            700, 6000],
    'Population (Millions)': [331, 1438, 126, 83, 1367, 66,
                              65, 213, 60, 38, 145, 51,
                              47, 25, 128, 273, 17,
                              34, 84, 8]
}

df = pd.DataFrame(data)

# Plotting the bubble chart
plt.figure(figsize=(14, 10))
bubble_chart = sns.scatterplot(data=df,
                               x='Research Budget (% GDP)',
                               y='Number of Researchers (per Million)',
                               size='Population (Millions)',
                               hue='Research Budget (% GDP)',
                               palette=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'],
                               sizes=(50, 1000),
                               alpha=0.7)

plt.title('Research and Development Investment by Country', fontsize=16, pad=20)
plt.xlabel('Research Budget (% GDP)', fontsize=14)
plt.ylabel('Number of Researchers (per Million)', fontsize=14)
plt.legend(loc='upper left', title='Population (Millions)')

# Show the final plot
plt.show()