
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Year': list(range(2000, 2021)),
    'Temperature': [
        15.1, 15.3, 15.5, 15.4, 15.6, 16.1, 16.2,
        16.8, 16.6, 17.0, 17.2, 17.1, 17.5, 17.7,
        18.1, 18.3, 18.7, 19.1, 19.4, 19.6, 20.1
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the size of the plot
plt.figure(figsize=(12, 6))

# Create the line chart
line_chart = sns.lineplot(data=df, x='Year', y='Temperature', marker='o', color='#FF6347', linewidth=2)

# Annotate specific points with a loop
for i in range(df.shape[0]):
    plt.text(x=df['Year'][i], y=df['Temperature'][i] + 0.1, s=f"{df['Temperature'][i]}", ha='center')

# Set the title and labels
plt.title('Global Average Temperature Over Time', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Temperature (°C)', fontsize=14)

# Show the plot
plt.show()