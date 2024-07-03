
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import squarify

# Create a DataFrame with the data
data = {
    'Sport': ['Soccer', 'Cricket', 'Basketball', 'Field Hockey', 'Tennis', 'Volleyball', 'Table Tennis', 'Baseball', 'Rugby', 'Golf', 'Badminton', 'Cycling', 'Boxing', 'Snooker', 'Wrestling'],
    'Viewership': [3500, 2500, 2400, 2000, 1500, 1400, 1200, 1000, 950, 900, 850, 800, 750, 700, 650],
    'Category': ['Team', 'Team', 'Team', 'Team', 'Individual', 'Team', 'Individual', 'Team', 'Team', 'Individual', 'Individual', 'Individual', 'Individual', 'Individual', 'Individual']
}
df = pd.DataFrame(data)

# Plot parameters
plt.figure(figsize=(14, 10))
cmap = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf',
        '#aec7e8', '#ffbb78', '#98df8a', '#ff9896', '#c5b0d5']

# Create a treemap
squarify.plot(sizes=df['Viewership'], label=df['Sport'], color=cmap, alpha=0.8)

plt.title('Popular Sports by Global Viewership', fontsize=18)
plt.axis('off')

plt.show()