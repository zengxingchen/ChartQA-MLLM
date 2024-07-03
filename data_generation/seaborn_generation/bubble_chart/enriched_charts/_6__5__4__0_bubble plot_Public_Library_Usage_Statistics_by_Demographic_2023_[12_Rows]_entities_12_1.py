
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Country': ['USA', 'China', 'India', 'Germany', 'France', 'Brazil', 'Canada', 'Russia', 'Australia', 'Japan', 'UK', 'South Korea', 'Italy', 'Spain', 'Netherlands'],
    'NumberOfUniversities': [6000, 4500, 4000, 2000, 1500, 2500, 1200, 1800, 1300, 1500, 1400, 1200, 1000, 900, 800],
    'ResearchPublications': [300000, 250000, 150000, 90000, 85000, 70000, 95000, 50000, 80000, 110000, 100000, 75000, 60000, 55000, 50000],
    'Investment': [1200, 900, 700, 600, 500, 300, 400, 350, 300, 700, 500, 400, 300, 280, 250]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(20, 16))
bubble = sns.scatterplot(data=df, x='ResearchPublications', y='NumberOfUniversities', size='Investment', hue='Country', 
                         palette=['#FF5733', '#33FF57', '#3357FF', '#FF33FB', '#57FFC1', '#FFD133', '#8333FF', 
                                  '#33FFF7', '#FF335B', '#FF9733', '#7333FF', '#33FF97', '#737373', '#FF57A6', '#57FF33'], 
                         sizes=(100, 2000), alpha=0.7, edgecolor='black')

plt.title('Number of Universities and Research Publications by Country in 2023', fontsize=24)
plt.xlabel('Research Publications', fontsize=18)
plt.ylabel('Number of Universities', fontsize=18)

# Customize legend
hand, labl = bubble.get_legend_handles_labels()
bubble.legend(hand[1:], labl[1:], title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()