
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Your given data table
data = [
    {'Age Group': '<18', 'Screen Time (hours)': 3.5},
    {'Age Group': '<18', 'Screen Time (hours)': 7.0},
    {'Age Group': '<18', 'Screen Time (hours)': 4.0},
    {'Age Group': '<18', 'Screen Time (hours)': 5.5},
    {'Age Group': '<18', 'Screen Time (hours)': 2.5},
    {'Age Group': '<18', 'Screen Time (hours)': 6.0},
    {'Age Group': '<18', 'Screen Time (hours)': 6.5},
    {'Age Group': '<18', 'Screen Time (hours)': 4.2},
    {'Age Group': '<18', 'Screen Time (hours)': 5.8},
    {'Age Group': '<18', 'Screen Time (hours)': 7.5},
    {'Age Group': '18-24', 'Screen Time (hours)': 8.0},
    {'Age Group': '18-24', 'Screen Time (hours)': 6.5},
    {'Age Group': '18-24', 'Screen Time (hours)': 7.2},
    {'Age Group': '18-24', 'Screen Time (hours)': 9.0},
    {'Age Group': '18-24', 'Screen Time (hours)': 5.5}
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Adjust the aesthetics of the plot for better visibility
sns.set(style="whitegrid")

# Create a histogram with Seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Screen Time (hours)', hue='Age Group', multiple="stack", bins=10, kde=False, palette='viridis')

# Additional customizations
plt.title('Screen Time Distribution by Age Group')
plt.xlabel('Screen Time (hours)')
plt.ylabel('Frequency')
plt.legend(title='Age Group')

# Show the plot
plt.show()