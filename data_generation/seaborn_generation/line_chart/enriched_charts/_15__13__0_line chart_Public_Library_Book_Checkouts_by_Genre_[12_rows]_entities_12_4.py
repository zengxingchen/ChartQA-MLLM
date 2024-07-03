
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Prepare the data
data = {
    'Year': list(range(2000, 2021)),
    'Popularity': [50, 55, 53, 60, 62, 65, 67, 70, 75, 77, 80, 83, 85, 87, 90, 92, 95, 97, 98, 99, 100]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set the style
sns.set_style("whitegrid")

# Create the line chart
plt.figure(figsize=(12, 6))
ax = sns.lineplot(x='Year', y='Popularity', data=df, color='#ff7f0e', linewidth=2.5)

# Annotating the last data point
plt.text(x=df['Year'].iloc[-1], y=df['Popularity'].iloc[-1], s=f"{df['Popularity'].iloc[-1]}%", 
         color='#ff7f0e', va='center', ha='right', fontsize=12)

# Setting the title and labels
plt.title('Music Popularity Trend (2000-2020)', fontsize=18, loc='center')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Popularity Index', fontsize=14)

# Display the plot
plt.show()