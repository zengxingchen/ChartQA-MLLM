
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Year': list(range(2000, 2021)),
    'Happiness_Index': [
        6.5, 6.7, 6.8, 7.0, 7.2, 7.1, 7.3, 7.5, 7.6, 7.7, 
        7.9, 8.0, 8.1, 8.3, 8.4, 8.5, 8.6, 8.7, 8.9, 9.0, 9.1
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 7))

# Create the line chart
line_chart = sns.lineplot(data=df, x='Year', y='Happiness_Index', marker='o', color='#4B0082', linewidth=2)

# Annotate specific points with a loop
for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Happiness_Index'][i] + 0.1, s=f"{df['Happiness_Index'][i]}", ha='center')

# Set the title and labels
plt.title('Global Happiness Index Over Time', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Happiness Index', fontsize=14)

# Show the plot
plt.show()