
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Event": [
        "First Modern Olympic Games", 
        "First FIFA World Cup", 
        "First Super Bowl", 
        "First NBA Game", 
        "First World Series", 
        "First Tour de France", 
        "First Wimbledon Championship", 
        "First Masters Tournament", 
        "First Boston Marathon", 
        "First Ironman Triathlon", 
        "First Cricket World Cup", 
        "First Rugby World Cup", 
        "First Formula 1 Race"
    ],
    "Year": [
        1896, 
        1930, 
        1967, 
        1946, 
        1903, 
        1903, 
        1877, 
        1934, 
        1897, 
        1978, 
        1975, 
        1987, 
        1950
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
fig, ax = plt.subplots(figsize=(16, 12))

# Area chart
ax.fill_between(df['Event'], df['Year'], color='#1f77b4', alpha=0.7)

# Titles and labels
ax.set_title('Historical Milestones in Sports', fontsize=22, pad=40)
ax.set_xlabel('Sports Event', fontsize=18)
ax.set_ylabel('Year', fontsize=18)

# Annotations
for i, txt in enumerate(df['Year']):
    ax.annotate(txt, (df['Event'][i], df['Year'][i]), textcoords="offset points", xytext=(0,5), ha='center')

# Display the plot
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()