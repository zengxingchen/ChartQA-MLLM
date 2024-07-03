
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Given dataset
data = {
    'Player': ['LeBron James', 'Stephen Curry', 'Kevin Durant', 'James Harden', 'Giannis Antetokounmpo',
               'Luka Dončić', 'Kawhi Leonard', 'Anthony Davis', 'Nikola Jokić', 'Damian Lillard'],
    'Points per Game': [27, 32, 29, 25, 28, 27, 24, 23, 26, 28]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize a Matplotlib figure and set its size
plt.figure(figsize=(12, 6))

# Create vertical bar chart
sns.barplot(
    x='Player',
    y='Points per Game',
    data=df,
    palette=[
        '#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F',
        '#EDC948', '#B07AA1', '#FF9DA7', '#9C755F', '#BAB0AC'
    ],
    dodge=False
)

# Customize the chart
plt.title('Top NBA Players by Points per Game')
plt.xlabel('Player')
plt.ylabel('Points per Game')

# Adjust the width of the bars
for patch in plt.gca().patches:
    patch.set_width(0.4)

# Show the plot
plt.show()