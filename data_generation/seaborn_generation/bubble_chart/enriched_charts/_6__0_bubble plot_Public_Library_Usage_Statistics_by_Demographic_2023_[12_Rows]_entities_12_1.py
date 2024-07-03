
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Country': ['France', 'Spain', 'USA', 'China', 'Italy', 'Turkey', 'Mexico', 'Germany', 'Thailand', 'UK', 'Japan'],
    'Visitors': [89.4, 82.7, 79.6, 65.7, 62.1, 45.8, 41.4, 39.6, 38.3, 37.9, 31.2],
    'Spending': [58.7, 55.6, 211.2, 40.3, 44.2, 34.5, 24.8, 36.7, 57.1, 32.5, 48.9],
    'AverageStay': [7.5, 7.2, 18.1, 9.5, 6.7, 5.6, 6.1, 5.9, 8.4, 6.3, 10.3]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(16, 12))
bubble = sns.scatterplot(data=df, x='Visitors', y='Spending', size='AverageStay', hue='Country', palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#57FFC1', '#FFD133', '#8333FF', '#33FFF7', '#FF335B', '#FF9733', '#737373'], sizes=(100, 2000), alpha=0.7, edgecolor='black')

plt.title('Tourist Visits and Spending by Country', fontsize=18)
plt.xlabel('Visitors (Millions)', fontsize=14)
plt.ylabel('Spending (Billion USD)', fontsize=14)

# Customize legend
hand, labl = bubble.get_legend_handles_labels()
bubble.legend(hand[1:], labl[1:], title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()