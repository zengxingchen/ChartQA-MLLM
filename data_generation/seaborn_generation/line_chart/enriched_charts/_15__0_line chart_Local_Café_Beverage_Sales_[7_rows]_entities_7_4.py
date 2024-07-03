
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Year': list(range(2000, 2021)),
    'Steps': [
        5000, 5200, 4800, 5300, 5500, 5700, 5900,
        6000, 6200, 6100, 6300, 6500, 6700, 6900,
        6800, 7000, 7100, 7300, 7500, 7400, 7600
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(14, 7))

# Create the line chart
line_chart = sns.lineplot(data=df, x='Year', y='Steps', marker='o', color='#4682B4', linewidth=2)

# Annotate specific points with a loop
for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Steps'][i] + 50, s=f"{df['Steps'][i]}", ha='center')

# Set the title and labels
plt.title('Average Daily Steps Over Time', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Steps', fontsize=14)

# Show the plot
plt.show()