
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Year': list(range(2000, 2021)),
    'Research_Advancements': [
        3.5, 3.6, 3.8, 4.0, 4.3, 4.7, 4.9, 5.1, 5.0, 4.8, 
        4.5, 4.6, 4.9, 5.3, 5.6, 6.0, 6.2, 6.5, 6.7, 7.0, 7.3
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 8))

# Create the line chart
line_chart = sns.lineplot(data=df, x='Year', y='Research_Advancements', marker='o', color='#1E90FF', linewidth=2)

# Annotate specific points with a loop
for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Research_Advancements'][i] + 0.1, s=f"{df['Research_Advancements'][i]}", ha='center')

# Set the title and labels
plt.title('Advancements in Scientific Research Over Time', fontsize=18, pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Research Advancements', fontsize=14)

# Show the plot
plt.show()