
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Area': ['North America', 'South America', 'Europe', 'Africa', 'Asia', 'Australia', 'Antarctica'],
    'Average_Temperature': [16, 25, 12, 27, 22, 20, -50]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(14, 8))  # Width and height modification
sns.barplot(x="Average_Temperature", y="Area", data=df,
            palette=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#c4e17f'],
            dodge=False)  # Color modification using specific color codes

# Set the bars' height
for bar in plt.gca().patches:
    bar.set_height(0.5)  # Height of bars when horizontal

plt.xlabel('Average Temperature (°C)')
plt.ylabel('Area')
plt.title('Average Temperature by Continent')
sns.despine(left=True, bottom=True)  # Cleaning up the plot
plt.show()