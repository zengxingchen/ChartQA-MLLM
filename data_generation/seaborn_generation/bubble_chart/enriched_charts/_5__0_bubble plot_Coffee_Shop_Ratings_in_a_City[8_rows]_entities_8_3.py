
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Prepare the data in a Pandas DataFrame
data = {
    'Species': ['Elephant', 'Blue Whale', 'Giraffe', 'Gorilla', 'Tiger', 'Kangaroo', 'Penguin', 'Eagle', 'Dolphin', 'Panda', 'Wolf'],
    'Weight (kg)': [6000, 140000, 1200, 160, 220, 85, 30, 6, 150, 100, 50],
    'Lifespan (years)': [70, 80, 25, 35, 20, 23, 20, 30, 40, 20, 15],
    'Population (millions)': [0.5, 0.01, 2, 0.1, 0.05, 50, 12, 0.7, 0.6, 0.02, 0.3]
}
df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(16, 10))
bubble = sns.scatterplot(data=df, x='Weight (kg)', y='Lifespan (years)', size='Population (millions)', hue='Species', 
                         palette=['#FF5733','#33FF57','#3357FF','#57FF33','#FF3357','#FFFF33','#33FFFF','#FF33FF','#333FFF','#33FF3F','#3F33FF'], 
                         sizes=(50, 1500), alpha=0.7, edgecolor='w', linewidth=0.5)

# Customize the axes and title
plt.title('Species Characteristics: Weight vs. Lifespan Population Bubble Chart', fontsize=20, pad=20)
plt.xlabel('Average Weight (kg)', fontsize=15)
plt.ylabel('Average Lifespan (years)', fontsize=15)

# Adjust legend
bubble.legend(loc='upper right', bbox_to_anchor=(1.2, 1), title='Species')

# Show the bubble chart
plt.show()