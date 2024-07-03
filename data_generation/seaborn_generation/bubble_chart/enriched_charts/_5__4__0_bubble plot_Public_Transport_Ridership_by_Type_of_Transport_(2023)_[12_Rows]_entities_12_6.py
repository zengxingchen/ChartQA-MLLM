
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame from the above data
data = {
    'Country': ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Brazil', 'Canada',
                'Australia', 'Russia', 'South Korea', 'Mexico', 'Indonesia', 'Turkey', 'Saudi Arabia', 'South Africa'],
    'GDP': [21433, 14140, 5065, 3846, 2875, 2827, 2715, 2001, 1839, 1643,
            1393, 1283, 1659, 1221, 1119, 755, 792, 351],
    'Population': [331, 1439, 126, 83, 1380, 67, 65, 60, 213, 38,
                   25, 145, 52, 128, 273, 84, 35, 59],
    'HappinessScore': [7.0, 5.1, 5.9, 6.7, 4.2, 7.2, 6.4, 6.0, 6.3, 7.6,
                       7.3, 5.4, 5.9, 6.5, 5.3, 5.2, 6.4, 4.6]
}
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(16, 12))

# Create the bubble chart
bubble = sns.scatterplot(data=df, x='HappinessScore', y='GDP', size='Population', 
                         hue='Country', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', 
                                                 '#33FFFB', '#FFFB33', '#FBFF33', '#837FF3',
                                                 '#8FF73F', '#3FF786', '#FF3333', '#3333FF',
                                                 '#33FFFF', '#FF33A1', '#A1FF33', '#3333A1',
                                                 '#A133FF', '#33A1FF'],
                         sizes=(100, 2000), alpha=0.7, edgecolor='w', linewidth=1)
bubble.set_title('Top Countries by GDP, Population, and Happiness Score in 2023', weight='bold', size=18, pad=20)
bubble.set_xlabel('Average Happiness Score', weight='bold', size=14)
bubble.set_ylabel('GDP (in billions USD)', weight='bold', size=14)

# Adjust legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

# Show the plot
plt.show()